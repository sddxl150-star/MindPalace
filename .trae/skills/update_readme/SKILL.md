---
name: "update_readme"
description: "Scans project file structure and auto-generates/updates README.md. Invoke when user asks to update, refresh, or generate README."
---

# README Updater

Automatically scans the project directory structure and generates or updates the README.md file based on the discovered files and folders.

## When to Use

- User asks to "update README", "refresh README", or "generate README"
- User wants to sync README with current project structure
- Project structure has changed and README needs to reflect current state

## How It Works

1. Scans the project root for all HTML files
2. Reads existing README.md navigation section
3. Compares HTML files against README links to detect missing pages
4. Updates README with:
   - Correct web page statistics
   - Missing pages added to appropriate navigation sections
   - Navigation序号(序号) updated to be continuous

## Output Format

The updated README includes:

- **Stats Section**: Auto-corrected web page count based on actual HTML files in project
- **Navigation**: All HTML pages listed with correct 序号, missing pages automatically added
- **序号 Consistency**: All 序号 in navigation tables are continuous (1, 2, 3... not 1, 2, 5, 6...)

### Key Features

- **Missing Page Detection**: Compares project HTML files against README links
- **Auto-Add**: New HTML files not in README are added to appropriate sections
- **序号 Repair**: Fixes any broken 序号 sequences in navigation tables

## Notes

- AI executes the README update directly using available tools (Read, Write, Edit, Glob, Grep)
- Ignores common non-page files: admin.html, offline.html
- Uses context clues from filename/section to place new pages in appropriate navigation category
- Always maintains continuous 序号 numbering in all navigation tables
