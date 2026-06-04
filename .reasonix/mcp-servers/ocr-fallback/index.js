#!/usr/bin/env node
// OCR MCP Server — Fallback (Tesseract.js)
// Plan B when PaddleOCR AI Studio is unavailable
// Supports: image file paths, base64 strings, URLs

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { createWorker } from "tesseract.js";
import fs from "fs";
import path from "path";

const server = new Server(
  { name: "ocr-fallback", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// Lazy init worker
let worker = null;
async function getWorker(lang = "chi_sim+eng") {
  if (!worker) {
    worker = await createWorker(lang, 1, {
      logger: () => {}, // silent
    });
  }
  return worker;
}

// Download image from URL
async function downloadImage(url) {
  try {
    const resp = await fetch(url);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    return Buffer.from(await resp.arrayBuffer());
  } catch (e) {
    throw new Error(`Failed to download image: ${e.message}`);
  }
}

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "ocr_image",
      description:
        "Extract text from an image using Tesseract.js OCR. Supports local file paths, http/https URLs, and base64 data URIs. Supports Chinese (chi_sim) and English (eng) by default. Returns the recognized text.",
      inputSchema: {
        type: "object",
        properties: {
          image: {
            type: "string",
            description:
              "Image source: local file path (e.g. C:\\Users\\...\\image.png), URL (https://...), or base64 data URI (data:image/png;base64,...)",
          },
          lang: {
            type: "string",
            description: "OCR language(s), e.g. 'chi_sim', 'eng', 'chi_sim+eng' (default)",

            default: "chi_sim+eng",
          },
        },
        required: ["image"],
      },
    },
    {
      name: "ocr_file",
      description:
        "Extract text from a local image file. Simplified wrapper — just pass the file path.",
      inputSchema: {
        type: "object",
        properties: {
          path: {
            type: "string",
            description: "Local file path to the image (PNG, JPG, etc.)",
          },
          lang: {
            type: "string",
            description: "OCR language(s), default 'chi_sim+eng'",
            default: "chi_sim+eng",
          },
        },
        required: ["path"],
      },
    },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    if (name === "ocr_image" || name === "ocr_file") {
      let imageData;
      const lang = args?.lang || "chi_sim+eng";

      if (name === "ocr_file") {
        const filePath = args?.path;
        if (!filePath) throw new Error("File path is required");
        if (!fs.existsSync(filePath)) throw new Error(`File not found: ${filePath}`);
        imageData = fs.readFileSync(filePath);
      } else {
        const source = args?.image;
        if (!source) throw new Error("Image source is required");

        if (source.startsWith("data:")) {
          // base64 data URI
          const base64 = source.split(",")[1];
          imageData = Buffer.from(base64, "base64");
        } else if (source.startsWith("http://") || source.startsWith("https://")) {
          // URL
          imageData = await downloadImage(source);
        } else {
          // Local file path
          const resolved = path.resolve(source);
          if (!fs.existsSync(resolved)) throw new Error(`File not found: ${resolved}`);
          imageData = fs.readFileSync(resolved);
        }
      }

      const w = await getWorker(lang);
      const { data } = await w.recognize(imageData);

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify({
              text: data.text,
              confidence: data.confidence,
              lang: lang,
              lines: data.text.split("\n").filter((l) => l.trim()),
            }, null, 2),
          },
        ],
      };
    }

    throw new Error(`Unknown tool: ${name}`);
  } catch (error) {
    return {
      content: [{ type: "text", text: `OCR Error: ${error.message}` }],
      isError: true,
    };
  }
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("OCR Fallback MCP Server started");
}

main().catch((err) => {
  console.error("Fatal:", err);
  process.exit(1);
});
