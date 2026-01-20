# Simple BRD Converter - Guide

## What It Does

Converts Excel files to CSV format for LLM processing.

## Installation

```bash
pip install openpyxl --break-system-packages
```

## Usage

### Command Line

```bash
# Print to screen
python brd_converter.py BRD_input.xlsx

# Save to file
python brd_converter.py input.xlsx output.csv

# Specific sheet
python brd_converter.py input.xlsx output.csv "Requirements"
```

### Python Code

```python
from brd_converter import excel_to_csv, convert_file

# Get CSV string
csv_string = excel_to_csv('brd.xlsx')

# Save to file
convert_file('brd.xlsx', 'output.csv')

# Specific sheet
csv_string = excel_to_csv('brd.xlsx', sheet_name='Requirements')
```

## Output Format

- Each cell separated by comma
- Each row separated by newlines
- Empty cells are blank: `value1,,value3`
- Images noted as: `[IMAGE at B5]`

## Example

**Excel:**
```
| Project | Portal |
| Version | 1.2    |
|         |        |
| ID      | Desc   |
```

**CSV Output:**
```
Project,Portal
Version,1.2
,
ID,Desc
```

## Pass to LLM

```python
csv_data = excel_to_csv('brd.xlsx')

prompt = f"""Convert this CSV data to Confluence markdown:

{csv_data}

Generate a well-formatted markdown document."""

# Send to LLM for conversion
```

## How It Works

1. Load Excel with openpyxl
2. Iterate every cell (left → right, top → bottom)
3. Extract images and note their location
4. Join cells with commas, rows with newlines
5. Output CSV string

## Limitations

- Images are noted but not extracted (shows location only)
- No formatting preservation
- Commas in cell values are escaped as `\,`
- Only processes one sheet at a time

## Next Steps

1. Convert Excel to CSV
2. Pass CSV to LLM (Claude Code, API, etc.)
3. LLM generates Confluence markdown
4. Upload markdown to Confluence via MCP
