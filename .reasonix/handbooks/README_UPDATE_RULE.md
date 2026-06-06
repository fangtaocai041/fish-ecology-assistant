# 📋 README Auto-Update Rule (README 自动更新规则)

> **Purpose**: Whenever new features are added (MCP tools, Skills, config sections, handbook docs, deployment files), the README.md AND README.zh.md MUST be updated in lockstep across BOTH projects.
> **Trigger**: Any commit that adds/modifies a feature visible in the README.

---

## PREFLIGHT (MANDATORY)

1. READ both `README.md` and `README.zh.md` for the project being modified
2. IDENTIFY which sections need updating based on the change type below

---

## Change Type → README Section Mapping

| Change Type | EN Section | ZH Section | What to Update |
|------------|-----------|-----------|----------------|
| **New MCP tool** | `## 📡 MCP Services (N Tools)` | `## 📡 MCP 服务（N 个工具）` | Add row to table, increment N in header |
| **New Skill** | `### Domain Specialists` | `### 领域专家` | Add row to table, increment count in header subtitle |
| **New config section** | `## 📁 Project Structure` | `## 📁 项目结构` | Add file to tree |
| **New handbook doc** | `## 📁 Project Structure` | `## 📁 项目结构` | Add file to `handbooks/` tree |
| **New deployment file** | `## 📁 Project Structure` | `## 📁 项目结构` | Add `Dockerfile`/`.github/` to tree |
| **New philosophy doc** | `## 📁 Project Structure` | `## 📁 项目结构` | Add doc to `docs/` or `handbooks/` tree |
| **Rule count change** | Header subtitle `<p>` | Header subtitle `<p>` | Update count in stats line |
| **Total MCP count** | `categories.total` | `categories.total` | Update in config AND capability table |

## Update Protocol

### Step 1: Identify all affected sections

```
FOR each change in the commit:
  MATCH change_type → section mapping
  COLLECT all affected sections for both README.md and README.zh.md
```

### Step 2: Update EN README first

```
1. Find the target section in README.md
2. Apply the update (add row / update count / add file to tree)
3. Verify the update is correct
```

### Step 3: Update ZH README in lockstep

```
1. Find the CORRESPONDING section in README.zh.md
2. Apply the SAME logical change (translated to Chinese)
3. Verify both READMEs are consistent
```

### Step 4: Cross-project sync (if applicable)

```
IF the change applies to BOTH fish-ecology-assistant AND porpoise-agent:
  REPEAT Steps 1-3 for the other project
```

## Consistency Checklist

After every README update, verify:

- [ ] EN and ZH README have the SAME number of MCP tools listed
- [ ] EN and ZH README have the SAME number of Skills listed
- [ ] Header subtitle counts match the actual table counts
- [ ] Project structure tree includes ALL new files
- [ ] Capability comparison table numbers match header counts
- [ ] Both projects have consistent counts (if shared feature)

## Examples

### Example 1: Adding a new MCP tool

```
Change: Added `deepwiki` MCP server
↓
EN README: `## 📡 MCP Services (16 Tools)` → `(18 Tools)`, add `deepwiki` row
ZH README: `## 📡 MCP 服务（16 个工具）` → `（18 个工具）`, add `deepwiki` row
Header: `16 MCP tools` → `18 MCP tools` (EN) / `16 MCP 工具` → `18 MCP 工具` (ZH)
```

### Example 2: Adding a new Skill

```
Change: Added `rule-auditor` Skill
↓
EN README: `### Domain Specialists` → add `rule-auditor` row
ZH README: `### 领域专家` → add `rule-auditor` row
Header: `12 AI subagents` → `14 AI subagents` (EN) / `12 AI 子智能体` → `14 AI 子智能体` (ZH)
```

### Example 3: Adding a new handbook

```
Change: Added `engineering-grammar.md`
↓
EN README: `## 📁 Project Structure` → add to `handbooks/` tree
ZH README: `## 📁 项目结构` → add to `handbooks/` tree
```

---

> **Rule**: One feature change → update BOTH languages in BOTH projects (if applicable). No exceptions.

**Last updated: 2026-06-06**
