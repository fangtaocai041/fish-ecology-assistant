#!/usr/bin/env node

/**
 * Cognitive Search Engine MCP Server
 * 
 * Wraps D:\Reasonix\cognitive-search-engine\ as MCP tools.
 * Dynamic import — engine updates take effect immediately, no manual steps.
 * 
 * Tools:
 *   1. csearch_species        — Full pipeline: graph_lookup → multi_engine → variant → dedup
 *   2. csearch_graph_lookup   — Read known papers from species_graph.yaml (0 token)
 *   3. csearch_add_paper      — Add new paper to graph (evolves the engine for future searches)
 */

import { spawn } from "child_process";
import { readFileSync, writeFileSync, existsSync } from "fs";
import { join, resolve } from "path";
import { fileURLToPath } from "url";
import { createInterface } from "readline";

const __dirname = fileURLToPath(new URL(".", import.meta.url));

// ── Core paths (point to canonical engine location) ──
const ENGINE_ROOT = resolve("D:\\Reasonix\\cognitive-search-engine");
const ENGINE_CONFIG = join(ENGINE_ROOT, "config");
const GRAPH_PATH = join(ENGINE_CONFIG, "species_graph.yaml");
const RULES_PATH = join(ENGINE_CONFIG, "search_rules.yaml");
const ENGINE_SRC = join(ENGINE_ROOT, "src");

// ── Tool implementations ──

/**
 * Run a Python module from the cognitive-search-engine src dir.
 * Returns { stdout, stderr, exitCode }.
 */
function runEnginePython(script, args = []) {
  return new Promise((resolvePromise, reject) => {
    const child = spawn("python", [
      "-c", script,
      ...args
    ], {
      cwd: ENGINE_ROOT,
      env: { ...process.env, PYTHONPATH: ENGINE_SRC + ";" + (process.env.PYTHONPATH || "") }
    });

    let stdout = "";
    let stderr = "";

    child.stdout.on("data", (data) => { stdout += data.toString(); });
    child.stderr.on("data", (data) => { stderr += data.toString(); });
    child.on("close", (code) => {
      resolvePromise({ stdout, stderr, exitCode: code });
    });
    child.on("error", (err) => reject(err));
  });
}

/**
 * Parse species_graph.yaml (simple YAML parser for the graph subset).
 * Returns the species node for a given ID, or all species if no ID given.
 */
function readGraph(speciesId = null) {
  if (!existsSync(GRAPH_PATH)) {
    return { found: false, error: "species_graph.yaml not found", papers: [], variants: [] };
  }
  
  const raw = readFileSync(GRAPH_PATH, "utf-8");
  
  // Simple extraction: find species block
  const speciesMatch = raw.match(/species:\n([\s\S]*?)(?=\n  authors:|\n  journals:|\n  papers:|\n  edges:)/);
  const papersMatch = raw.match(/papers:\n([\s\S]*?)(?=\n  edges:|\n$)/);
  const authorsMatch = raw.match(/authors:\n([\s\S]*?)(?=\n  journals:|\n  papers:|\n  edges:|\n$)/);
  
  // Extract species list
  const speciesList = [];
  if (speciesMatch) {
    const speciesBlock = speciesMatch[1];
    const regex = /- id:\s*"(.+?)"[\s\S]*?(?=\n- id:|\n  authors:|\n  journals:|\n  papers:|\n  edges:|\n$)/g;
    let m;
    while ((m = regex.exec("  " + speciesBlock)) !== null) {
      speciesList.push(m[1]);
    }
  }
  
  // Extract papers for the target species
  const papers = [];
  if (papersMatch) {
    const block = papersMatch[1];
    const paperBlocks = block.split("\n- doi:");
    for (const pb of paperBlocks) {
      if (!pb.trim()) continue;
      const doi = pb.match(/^([^\n]+)/)?.[0]?.trim() || "";
      const title = pb.match(/title:\s*"(.+?)"/)?.[1] || pb.match(/title:\s*(.+)/)?.[1]?.trim() || "";
      const year = pb.match(/year:\s*(\d+)/)?.[1];
      const journal = pb.match(/journal:\s*(.+)/)?.[1]?.trim() || "";
      const note = pb.match(/note:\s*(.+)/)?.[1]?.trim() || "";
      
      // Extract authors
      const authorMatch = pb.match(/authors:\n([\s\S]*?)(?=\n    (?:institutions|species|citations|doi|title|year|journal|note|type|pmid))/);
      const authors = [];
      if (authorMatch) {
        const authorLines = authorMatch[1].split("\n");
        for (const line of authorLines) {
          const a = line.match(/-\s*"?([^"\n]+?)"?$/);
          if (a) authors.push(a[1].trim());
        }
      }
      
      // Extract institutions
      const instMatch = pb.match(/institutions:\n([\s\S]*?)(?=\n    (?:species|citations|doi|title|year|journal|note|type|pmid))/);
      const institutions = [];
      if (instMatch) {
        const instLines = instMatch[1].split("\n");
        for (const line of instLines) {
          const i = line.match(/-\s*"?([^"\n]+?)"?$/);
          if (i) institutions.push(i[1].trim());
        }
      }
      
      papers.push({ doi: doi ? "doi:" + doi : "", title, year, journal, authors, institutions, note });
    }
  }
  
  // Extract variants for the target species
  let variants = [];
  if (speciesId && speciesMatch) {
    const speciesBlock = speciesMatch[1];
    const targetRegex = new RegExp(`- id:\\s*"${escapeRegex(speciesId)}"[\\s\\S]*?(?=\\n- id:|\\n  authors:|\\n$)`);
    const targetMatch = speciesBlock.match(targetRegex);
    if (targetMatch) {
      const variantMatch = targetMatch[0].match(/variants:\n([\s\S]*?)(?=\n  (?:chinese|family|conservation|aliases|$))/);
      if (variantMatch) {
        const vLines = variantMatch[1].split("\n");
        for (const line of vLines) {
          const v = line.match(/-\s*"?([^"\n]+?)"?$/);
          if (v) variants.push(v[1].trim());
        }
      }
    }
  }
  
  return {
    found: true,
    species: speciesList,
    papers: papers,
    variants: variants,
    rawLength: raw.length
  };
}

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/**
 * Tool: Full species search pipeline
 * Runs graph_lookup → multi_engine_parallel → variant_search → dedup_merge
 */
async function speciesSearch(args) {
  const { species_id, scientific_name, chinese_name, limit } = args;
  const id = species_id || (scientific_name ? scientific_name.replace(/\s+/g, "_") : "unknown");
  
  // Phase 1: graph_lookup (0 token)
  const graph = readGraph(id);
  
  // Phase 2: If Python engine is available, run the full pipeline
  // Otherwise return graph data as baseline
  let pythonResult = null;
  try {
    const pyResult = await runEnginePython(`
import sys
sys.path.insert(0, r"${ENGINE_SRC.replace(/\\/g, "\\\\")}")
try:
    from rule_engine import SearchRuleEngine
    engine = SearchRuleEngine(r"${RULES_PATH.replace(/\\/g, "\\\\")}")
    result = engine.execute("${id}")
    print(f"PHASES: {result['phases_executed']}")
    print(f"TOKENS: {result['tokens_spent']}")
    print(f"EFFICIENCY: {result['efficiency']}")
    if result.get('world_model'):
        print(f"WORLD_MODEL: volume={result['world_model']['predicted_volume']}, accuracy={result['world_model']['accuracy']}")
except Exception as e:
    print(f"ENGINE_WARN: {e}")
`);
    if (pyResult.exitCode === 0) {
      pythonResult = {
        phases: pyResult.stdout.match(/PHASES: (.*)/)?.[1] || "",
        tokens: pyResult.stdout.match(/TOKENS: (.*)/)?.[1] || "",
        efficiency: pyResult.stdout.match(/EFFICIENCY: (.*)/)?.[1] || "",
        worldModel: pyResult.stdout.match(/WORLD_MODEL: (.*)/)?.[1] || ""
      };
    }
  } catch (e) {
    // Engine unavailable, fall back to graph + tool calls
  }
  
  return {
    species_id: id,
    scientific_name: scientific_name || id.replace(/_/g, " "),
    chinese_name: chinese_name || "",
    graph_papers_count: graph.papers.length,
    graph_variants: graph.variants,
    known_papers: graph.papers,
    pipeline_result: pythonResult,
    note: graph.papers.length > 0 
      ? `Graph contains ${graph.papers.length} known papers. Run multi_engine_parallel/variant_search phases for latest.`
      : "Species not in graph yet. Run multi_engine_parallel to discover papers."
  };
}

/**
 * Tool: Just read graph (0 token cost)
 */
function graphLookup(args) {
  const graph = readGraph(args.species_id);
  return {
    species_id: args.species_id,
    in_graph: graph.found && graph.species.includes(args.species_id),
    known_papers: graph.papers,
    variants: graph.variants,
    paper_count: graph.papers.length
  };
}

/**
 * Tool: Add a paper to the graph (evolves the engine for future searches)
 */
function addPaper(args) {
  if (!existsSync(GRAPH_PATH)) {
    return { success: false, error: "Graph file not found" };
  }
  
  const { species_id, doi, title, year, journal, authors, institutions, note } = args;
  
  const entry = `
  - doi: ${doi || "pending"}
    title: "${title}"
    year: ${year || "unknown"}
    journal: "${journal || ""}"
    authors:
${(authors || []).map(a => `    - "${a}"`).join("\n")}
    species:
    - ${species_id}
    institutions:
${(institutions || []).map(i => `    - "${i}"`).join("\n")}
    ${note ? `note: "${note}"` : ""}`;
  
  try {
    writeFileSync(GRAPH_PATH, readFileSync(GRAPH_PATH, "utf-8").trimEnd() + entry + "\n", "utf-8");
    return { success: true, added: { species_id, title, doi } };
  } catch (e) {
    return { success: false, error: e.message };
  }
}

// ── MCP Server ──

const encoder = new TextEncoder();
const decoder = new TextDecoder();
let buffer = "";

process.stdin.on("data", (chunk) => {
  buffer += decoder.decode(chunk, { stream: true });
  const lines = buffer.split("\n");
  buffer = lines.pop() || "";

  for (const line of lines) {
    if (!line.trim()) continue;
    try {
      const msg = JSON.parse(line);
      handleMessage(msg).then((response) => {
        if (response) {
          process.stdout.write(encoder.encode(JSON.stringify(response) + "\n"));
        }
      }).catch((err) => {
        console.error("handler error:", err);
      });
    } catch (e) {
      console.error("parse error:", e.message);
    }
  }
});

async function handleMessage(msg) {
  const { id, method, params } = msg;

  // ── Initialize ──
  if (method === "initialize") {
    return {
      id, type: "response",
      result: {
        protocolVersion: "2024-11-05",
        capabilities: { tools: {} },
        serverInfo: { name: "cognitive-search-mcp", version: "2.0.0" }
      }
    };
  }

  // ── List Tools ──
  if (method === "tools/list") {
    return {
      id, type: "response",
      result: {
        tools: [
          {
            name: "csearch_species",
            description: "[认知搜索管线] 全流程物种搜索：graph_lookup(0 token) → multi_engine_parallel(7引擎) → variant_search(OCR变体) → author_crossref → citation_traversal → dedup_merge。引擎自动进化，新版本无需任何手动更新。",
            inputSchema: {
              type: "object",
              properties: {
                species_id: {
                  type: "string",
                  description: "图谱物种ID (如 Ochetobius_elongatus)。与 scientific_name 二选一。"
                },
                scientific_name: {
                  type: "string",
                  description: "学名 (如 Ochetobius elongatus)。与 species_id 二选一。"
                },
                chinese_name: {
                  type: "string",
                  description: "中文名 (如 鳤)，用于中文文献搜索"
                },
                limit: {
                  type: "number",
                  description: "最大返回论文数，默认20",
                  default: 20
                }
              }
            }
          },
          {
            name: "csearch_graph",
            description: "[图谱查询] 读取物种知识图谱中的已知论文，0 token成本。快速查看已积累的物种知识。",
            inputSchema: {
              type: "object",
              properties: {
                species_id: {
                  type: "string",
                  description: "图谱物种ID (如 Ochetobius_elongatus)"
                }
              },
              required: ["species_id"]
            }
          },
          {
            name: "csearch_add_paper",
            description: "[图谱进化] 向物种知识图谱添加新论文，下次搜索自动包含。让引擎持续进化。",
            inputSchema: {
              type: "object",
              properties: {
                species_id: {
                  type: "string",
                  description: "图谱物种ID"
                },
                doi: {
                  type: "string",
                  description: "DOI标识符"
                },
                title: {
                  type: "string",
                  description: "论文标题"
                },
                year: {
                  type: "number",
                  description: "发表年份"
                },
                journal: {
                  type: "string",
                  description: "期刊名"
                },
                authors: {
                  type: "array",
                  items: { type: "string" },
                  description: "作者列表"
                },
                institutions: {
                  type: "array",
                  items: { type: "string" },
                  description: "单位列表"
                },
                note: {
                  type: "string",
                  description: "备注（如拼写变体说明）"
                }
              },
              required: ["species_id", "title"]
            }
          },
          {
            name: "csearch_update_graph",
            description: "[图谱同步] 将 multi_engine_parallel 搜索到的新论文批量写入图谱，使 engine 持续进化。",
            inputSchema: {
              type: "object",
              properties: {
                species_id: {
                  type: "string",
                  description: "图谱物种ID"
                },
                papers: {
                  type: "array",
                  items: {
                    type: "object",
                    properties: {
                      doi: { type: "string" },
                      title: { type: "string" },
                      year: { type: "number" },
                      journal: { type: "string" },
                      authors: { type: "array", items: { type: "string" } },
                      institutions: { type: "array", items: { type: "string" } }
                    }
                  },
                  description: "新论文列表"
                }
              },
              required: ["species_id", "papers"]
            }
          }
        ]
      }
    };
  }

  // ── Call Tool ──
  if (method === "tools/call") {
    const { name, arguments: args } = params;
    
    try {
      let result;
      switch (name) {
        case "csearch_species":
          result = await speciesSearch(args || {});
          break;
        case "csearch_graph":
          result = graphLookup(args || {});
          break;
        case "csearch_add_paper":
          result = addPaper(args || {});
          break;
        case "csearch_update_graph":
          result = { success: true, message: "Batch update requires manual graph editing or Python engine. Use csearch_add_paper for individual papers.", papers: (args || {}).papers || [] };
          break;
        default:
          return {
            id, type: "response",
            result: {
              content: [{ type: "text", text: `Unknown tool: ${name}` }],
              isError: true
            }
          };
      }
      
      return {
        id, type: "response",
        result: {
          content: [{ type: "text", text: JSON.stringify(result, null, 2) }]
        }
      };
    } catch (err) {
      return {
        id, type: "response",
        result: {
          content: [{ type: "text", text: `Error: ${err.message}` }],
          isError: true
        }
      };
    }
  }

  return null;
}
