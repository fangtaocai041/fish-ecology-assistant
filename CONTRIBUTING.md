# Contributing

Thanks for your interest in improving reasonix-data!

## Ways to Contribute

- **Adapt for your domain**: Fork and customize for physics, medicine, law, or any field — then share back what you learned
- **Add new skills**: Built a useful subagent? Submit it as a new `.reasonix/skills/` playbook
- **Add new MCP services**: Found a great MCP server? Add the wrapper script + update `setup-migrate.ps1`
- **Port to Linux/macOS**: Replace `.bat` wrappers with shell scripts
- **Improve documentation**: Fix typos, add examples, clarify confusing sections
- **Report issues**: Found a bug or have an idea? Open an [issue](https://github.com/fangtaocai041/reasonix-data/issues)

## Project Structure

```
.reasonix/
├── mcp-servers/      ← MCP wrapper scripts & custom servers
├── skills/           ← AI subagent playbooks (12 markdown files)
└── setup-migrate.ps1 ← One-click new-machine migration
```

The key design principle: **subagent isolation**. Each skill runs in its own context — no shared token space.

## Adding a New Skill

1. Create `skill-name.md` in `.reasonix/skills/` with frontmatter:

```yaml
---
name: my-skill
description: One-line description of what it does
runAs: subagent
allowed-tools: web_search, scholar_search_literature_graph
---
# Skill Title

Your playbook content here...
```

2. Update the README Skills table
3. Update the Orchestrator if it's part of the pipeline

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
