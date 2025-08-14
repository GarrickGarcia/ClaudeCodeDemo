# CLAUDE.md

This file serves as memory documentation for claude code while working in this repository

## Repository Purpose

This repository serves as a **demonstration environment for Claude Code features**, showcasing automated script creation, debugging, and execution capabilities with ArcPy and GIS workflows.

## Repository Architecture

### Core Components

#### 1. Demo Scripts
- **`count_wMain_features.py`** - Simple static script that counts features in the wMain feature class
- **`bugged_arcpy.py`** - Intentionally bugged script for demonstrating debugging capabilities
  - Contains a logical error (attribute access instead of index notation)
  - Used to demonstrate Claude's ability to identify and fix bugs

#### 2. Demo Data
- **Location**: `Data/DemoData.gdb`
- **Feature Class**: `wMain` - Water main infrastructure data
  - 569 features representing water distribution pipes
  - Key fields:
    - `MATERIAL` - Pipe material type (8 unique types: CAS, CT, Cast Iron, DIP, GP, HDPE, PE, PVC)
    - `DIAMETER` - Pipe diameter in inches (2.0 to 16.0)
    - `Shape_Length` - Calculated geometry length (total: 146,288 units)
    - `LENGTH_FT` - Stored length in feet (mostly NULL - 99.6%)
    - `INSTALLDATE` - Installation date
    - Various maintenance and ownership fields

#### 3. Slash Commands (`.claude/commands/`)
Custom commands for reproducible demonstrations:

- **`/Make_Demo`** - Creates the count_wMain_features.py script
- **`/Create_Bugged_Script` (aliases: `/bugged`, `/create-bug`)** - Creates the intentionally bugged script
- **`/Fix_Bugged_Script` (aliases: `/fix-bug`, `/debug`)** - Fixes the bugged script with explicit instructions

#### 4. GitHub Actions Integration
- **Claude Code Review** (`.github/workflows/claude-code-review.yml`) - Automatically reviews pull requests
- **Claude Code** (`.github/workflows/claude.yml`) - Responds to @claude mentions in issues and PR comments

## Usage Guidelines

### Running Demo Scripts

1. **Execute scripts** using the `/run` command:
   ```
   /run @count_wMain_features.py
   /run @bugged_arcpy.py
   ```

2. **Python Environment**: Uses ArcGIS Pro conda environment
   - Path: `C:\Users\ggarcia\AppData\Local\ESRI\conda\envs\arcgispro-py3-vscode\python.exe`

### Demonstration Workflow

1. **Basic Feature Count**:
   - Run `/Make_Demo` to create the simple counting script
   - Execute with `/run @count_wMain_features.py`
   - Shows: 569 features in wMain

2. **Bug Fix Demonstration**:
   - Run `/Create_Bugged_Script` to create the bugged script
   - Attempt to run - will fail with AttributeError
   - Run `/Fix_Bugged_Script` to fix the bug
   - Execute again - will show material length summary

### Expected Outputs

- **count_wMain_features.py**: `wMain feature count: 569`
- **bugged_arcpy.py (fixed)**: Summary table showing total lengths by material type

## Development Notes

### Important Constraints
- **Read-only data**: Never modify the demo geodatabase
- **Simple outputs**: Keep results concise for terminal display
- **Error demonstration**: Bugs should cause actual failures, not just wrong results

### Script Requirements
- All scripts connect to: `C:\\Users\\ggarcia\\OneDrive - Abonmarche\\Documents\\GitHub\\ClaudeCodeDemo\\Data\\DemoData.gdb`
- Target feature class: `wMain`
- Use ArcPy data access cursors for operations
- Keep output formatted and readable in terminal

### Slash Command Structure
Commands in `.claude/commands/` must:
- Include explicit Python code in the markdown
- Provide clear instructions without requiring interpretation
- Include expected response messages
- Be fully reproducible

## Environment Details

- **Platform**: Windows (win32)
- **Workspace**: VS Code (ClaudeCodeDemo.code-workspace)
- **Python**: ArcGIS Pro Python 3.x with arcpy
- **Repository Branch**: main
- **Git Integration**: Configured with GitHub Actions for CI/CD