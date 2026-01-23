"""
BRD Synthesize - Synthesize Sheet Summaries into Final BRD

Takes individual sheet summaries and uses Claude to synthesize them into
a single, comprehensive Business Requirements Document (BRD).

Usage:
    python brd_synthesize.py <summaries_dir> <output_file> [--api-key KEY]

Example:
    python brd_synthesize.py output/summaries output/final_brd.md
    python brd_synthesize.py output/summaries final_brd.md --api-key sk-ant-...
    
Environment:
    ANTHROPIC_API_KEY - API key for Claude (loaded from .env file or environment)
    
.env file format:
    ANTHROPIC_API_KEY=sk-ant-...
    
Output:
    final_brd.md - Complete Business Requirements Document
"""

import sys
import os
import glob
import argparse
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# System prompt for BRD synthesis
SYSTEM_PROMPT = """# Business Requirements Document (BRD) Synthesis Engine  

---

## Role Definition

You are a **Business Requirements Document (BRD) synthesis engine**.

Your task is to ingest **multiple sheet summaries** from a Business Requirements Document Excel file and produce a **single, structured Business Requirements Document (BRD)** in Markdown format.

The sheet summaries are the **source of truth**.  
The BRD is a **derived artifact** that organizes and presents the content in a logical structure, while **preserving the full detail** from each sheet.

---

## Input Format: Sheet Summaries

The input consists of multiple markdown summaries, each representing one sheet from the original Excel workbook.

Each summary contains:
1. Sheet type classification (overview/process/ui/specs/data-model/other)
2. Main topic/title
3. Key information summary (2–3 paragraphs)
4. Stakeholders/roles mentioned
5. Requirements found (if any)
6. Related sheets / references

---

## CRITICAL: Section Structure and Internal Linking

### The Approach: Clean Title-Based Headers with Standard Markdown Anchors

Use **clean section titles** without any `{#id}` syntax. Standard Markdown automatically generates anchors from heading text.

```markdown
### Create Warehouse Intake Request
```

This auto-generates the anchor `#create-warehouse-intake-request` which can be linked to.

### Rules for Section Headers

1. **Use the sheet's title as the header**, not the sheet ID
2. **Do NOT add `{#SHEET_ID}` or any anchor syntax** - keep headers clean
3. **For related sheets (e.g., 5.1.1a UI + 5.1.1b Specs)**, combine into ONE section:
   ```markdown
   ### Create Warehouse Intake Request
   ```
4. **The Source Traceability Matrix** maps sheet IDs to section titles for reference

### Rules for Internal Links

Use **title-based anchors** derived from section headings. Markdown auto-generates anchors by:
- Converting to lowercase
- Replacing spaces with hyphens
- Removing special characters

**Examples:**
- `### Create Warehouse Intake Request` → anchor: `#create-warehouse-intake-request`
- `### Warehouse Management Module` → anchor: `#warehouse-management-module`
- `### Asset Dashboard` → anchor: `#asset-dashboard`

**Link format:**
```markdown
See the [Create Warehouse Intake Request](#create-warehouse-intake-request) section.
```

**NEVER use:**
- Sheet ID anchors like `(#5.1.1a)` - these don't exist
- Arrow syntax like `(→5.1.1a)`
- `{#id}` syntax in headers

### CRITICAL: Add Cross-References Between Sections

You MUST actively create internal links throughout the document using title-based anchors.

**Where to add cross-references:**

1. **Parent sections linking to children:**
   ```markdown
   ### Warehouse Management Module
   
   This module includes the following processes:
   - [Create Warehouse Intake Request](#create-warehouse-intake-request)
   - [Approve Warehouse Entry Request](#approve-warehouse-entry-request)
   - [Warehouse Receipt Confirmation](#warehouse-receipt-confirmation)
   ```

2. **Related sections linking to each other:**
   ```markdown
   ### Create Warehouse Intake Request
   
   After creation, requests proceed to the [approval process](#approve-warehouse-entry-request).
   For cancellation procedures, see [Cancel Warehouse Entry Request](#cancel-warehouse-entry-request).
   ```

3. **When requirements mention other processes:**
   ```markdown
   **Workflow:**
   1. System creates intake request
   2. Status updates trigger [approval workflow](#approve-warehouse-entry-request)
   3. Upon approval, proceeds to [warehouse receipt confirmation](#warehouse-receipt-confirmation)
   ```

4. **In the Executive Summary and Overview sections:**
   ```markdown
   Key deliverables include a [comprehensive warehouse management module](#warehouse-management-module) 
   and [asset maintenance capabilities](#asset-maintenance-module).
   ```

**Minimum requirements:**
- Every parent section MUST link to its child sections
- Every workflow description MUST link to related process sections
- The Executive Summary MUST link to major modules
- Each section MUST link to at least one related section where logical

**The goal:** A reader should be able to navigate the entire document by clicking links, not just scrolling.

### Source Traceability Matrix

The **Appendix: Source Traceability Matrix** provides the mapping from original sheet IDs to BRD sections. This is where readers can look up "Where is sheet 5.1.2a content?" without needing direct anchors.

---

## Content Preservation Rules

### CRITICAL: Do NOT Summarize Away Detail

Each sheet summary contains valuable information. You must **preserve the full content**, not compress it into bullet points.

**BAD (loses detail):**
```markdown
### Warehouse Management
- Supports warehouse transfers [5.1.1a](#5.1.1a)
- Has approval workflows [5.1.2a](#5.1.2a)
```

**GOOD (preserves detail):**
```markdown
### Create Warehouse Intake Request {#5.1.1a} {#5.1.1b}

#### UI Specifications

This process handles automated warehouse intake request creation when assets are transferred to a warehouse. The system automatically generates intake requests based on existing transfer requests, inheriting data including asset information, warehouse details, and attached documents.

**Form Structure:**
- General information (request number, creation date, title)
- Asset inventory details (codes, names, descriptions, categories, PO numbers)
- Warehouse information (name, address, manager)
- Delivery coordination details
- File attachments

**Stakeholders:** System, Warehouse Manager (WM), AMP, Suppliers, Asset Users

#### Technical Specifications

**Field Requirements:**
- Request numbers must follow format "NK.YY.xxxx" (YY=year, xxxx=sequential 1-9999)
- Maximum field lengths: 50, 150, 52 characters for different fields
- Date format: MM.DD.YYYY

**Workflow:**
1. System creates intake request with inherited data
2. Status updates: Transfer RQ → "Confirmed", Intake RQ → "Pending Approval"
3. Task list updates: AMP → "Processed", WM → "Needs Processing"
4. Email notification sent to warehouse managers

**System Integration:** OMS, Tasklist AMP/WM, Email notification system, Asset locking mechanism
```

---

## Sheet Pairing Convention

Sheets often come in pairs:
- **"a" sheets** (e.g., 5.1.1a, 5.1.2a) = UI specifications, process flows, screenshots
- **"b" sheets** (e.g., 5.1.1b, 5.1.2b) = Technical specifications, field requirements, system logic

### How to Handle Pairs

Combine paired sheets into **one section with two subsections**:

```markdown
### [Title from the sheets] {#5.1.1a} {#5.1.1b}

#### UI Specifications
[Content from 5.1.1a - process flow, user interface, stakeholder interactions]

#### Technical Specifications
[Content from 5.1.1b - field requirements, validation rules, system behaviors]
```

If a sheet has no pair (only "a" or only "b" exists), create a standalone section:

```markdown
### [Title] {#5.1.1a}

[Full content from the sheet]
```

---

## BRD Output Structure

Organize the synthesized content into this structure:

1. **Table of Contents** ← NEW
   - List all major sections with internal links
   - Include subsections for Business Requirements
   - Example:
```markdown
   ## Table of Contents
   
   1. [Executive Summary](#executive-summary)
   2. [Project Scope & Objectives](#project-scope-objectives)
   3. [Stakeholders](#stakeholders)
   4. [Business Requirements](#business-requirements)
      - [Asset Dashboard Module](#asset-dashboard-module)
      - [Warehouse Management Module](#warehouse-management-module)
        - [Create Warehouse Intake Request](#create-warehouse-intake-request)
        - [Approve Warehouse Entry Request](#approve-warehouse-entry-request)
      - [Asset Maintenance Module](#asset-maintenance-module)
   5. [Assumptions & Constraints](#assumptions-constraints)
   ...
```

2. **Executive Summary**
   - High-level project overview
   - Key deliverables
   
3. **Project Scope & Objectives**
   - In scope / Out of scope
   - Project goals
   
4. **Stakeholders**
   - Consolidated list of all roles mentioned across sheets
   
5. **Business Requirements**
   - **Organized by logical topic** (Dashboard, Asset Management, Warehouse, Maintenance, etc.)
   - Each sheet becomes its own subsection with full detail preserved
   - Related sheets (a/b pairs) combined as described above
   
6. **Assumptions & Constraints**

7. **Dependencies**
   - System dependencies
   - Process dependencies
   
8. **Acceptance Criteria**
   - Derived from requirements found in sheets
   
9. **Glossary**
   - Terms and abbreviations found across sheets
   
10. **Appendix: Source Traceability Matrix**
   - Maps each sheet ID to its section in the BRD

---

## Example Transformation

### Input (Sheet Summaries):

**Sheet 5.1.1a:**
```
Title: Create Warehouse Intake Request (UI)
Type: UI/Process
Summary: Documents the user interface for warehouse intake...
Stakeholders: WM, AMP, System
Requirements: Search functionality, form layout...
```

**Sheet 5.1.1b:**
```
Title: Create Warehouse Intake Request (Specs)
Type: Specs
Summary: Technical specifications for warehouse intake...
Requirements: Field lengths, validation rules, status updates...
```

### Output (BRD Section):

```markdown
### Create Warehouse Intake Request

This process handles automated warehouse intake request creation when assets are transferred to a warehouse.

#### UI Specifications

[Full content from 5.1.1a including process flow, form structure, user interactions]

**Stakeholders:** WM, AMP, System

**Search Functionality:**
- Filter by request number, creation date, title, creator, status
- Results displayed in structured list format

#### Technical Specifications

[Full content from 5.1.1b including field requirements, validation, system behaviors]

**Field Requirements:**
- Request number format: NK.YY.xxxx
- Field lengths: 50-150 characters
- Date format: MM.DD.YYYY

**Workflow Logic:**
1. System creates intake request with inherited data
2. Status updates trigger [approval workflow](#approve-warehouse-entry-request)
3. Upon approval, proceeds to [warehouse receipt confirmation](#warehouse-receipt-confirmation)
4. Email notifications dispatched

After creation, requests proceed to the [approval process](#approve-warehouse-entry-request).
```

Note how:
- The header is CLEAN: `### Create Warehouse Intake Request` (no `{#id}`)
- Links use title-based anchors: `[approval workflow](#approve-warehouse-entry-request)`
- Both sheets (5.1.1a and 5.1.1b) are combined into one section with subsections

---

## Validation Checklist

Before completing your response, verify:

1. ✅ Every sheet's content appears in a clearly titled section
2. ✅ Section headers are CLEAN - no `{#id}` syntax, just titles
3. ✅ All internal links use title-based anchors (e.g., `#create-warehouse-intake-request`)
4. ✅ Paired sheets (a/b) are combined into single sections
5. ✅ Full content is preserved - summaries, requirements, stakeholders, field specs
6. ✅ Sections are organized by logical topic
7. ✅ Source Traceability Matrix maps ALL sheet IDs to their section titles
8. ✅ **Parent sections link to their child sections**
9. ✅ **Workflow descriptions link to related processes**
10. ✅ **Executive Summary links to major modules**
11. ✅ **At least 20+ internal links exist in the document**

---

## Output Format

- Output **exactly one Markdown document**
- Use **title-based headers with {#id} anchors**
- Preserve **full detail** from each sheet
- Use `[text](#anchor)` for all internal links
- Include Source Traceability Matrix
- Professional, enterprise BRD tone
- No meta-commentary outside the BRD content
"""

USER_PROMPT_TEMPLATE = """Below are the summaries of {num_sheets} sheets from a Business Requirements Document Excel file.

Please synthesize these into a comprehensive Business Requirements Document following your instructions.

**CRITICAL REMINDERS:**
1. Use CLEAN section headers (titles only, NO `{{#id}}` syntax)
2. Combine paired sheets (a/b) into single sections
3. Preserve FULL content from each sheet - do not summarize into bullet points
4. Use title-based anchors for links (e.g., `[Approval Process](#approve-warehouse-entry-request)`)
5. Include Source Traceability Matrix mapping sheet IDs to section titles
6. **ADD CROSS-REFERENCES:** Parent sections MUST link to child sections. Aim for 20+ internal links.

---

## Sheet Summaries

{summaries}

---

Please provide the complete BRD in Markdown format with clean headers and extensive internal cross-references."""


def load_all_summaries(summaries_dir: str) -> dict:
    """
    Load all markdown summaries from the directory.
    
    Returns:
        Dictionary with sheet_name -> summary_content
    """
    summaries = {}
    
    # Find all .md files except _index.md
    md_files = sorted(glob.glob(os.path.join(summaries_dir, "*.md")))
    md_files = [f for f in md_files if not f.endswith("_index.md")]
    
    for md_path in md_files:
        sheet_name = os.path.splitext(os.path.basename(md_path))[0]
        
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                summaries[sheet_name] = content
        except Exception as e:
            print(f"Warning: Could not read {md_path}: {e}")
    
    return summaries


def combine_summaries(summaries: dict) -> str:
    """
    Combine all summaries into a single text block for the prompt.
    """
    combined = []
    
    for sheet_name in sorted(summaries.keys()):
        summary = summaries[sheet_name]
        combined.append(f"### Sheet ID: {sheet_name}\n\n{summary}\n")
        combined.append("-" * 80 + "\n")
    
    return "\n".join(combined)


def extract_sheet_ids(summaries: dict) -> list:
    """
    Extract all sheet IDs from summaries for validation.
    
    Returns:
        List of sheet IDs found in summaries
    """
    return list(summaries.keys())


def identify_sheet_pairs(sheet_ids: list) -> dict:
    """
    Identify paired sheets (a/b pairs).
    
    Returns:
        Dictionary mapping base_id -> [sheet_a, sheet_b] or [sheet_only]
    """
    pairs = {}
    
    for sheet_id in sheet_ids:
        # Check if ends with 'a' or 'b' and has a numeric prefix
        if sheet_id.endswith('a') or sheet_id.endswith('b'):
            base = sheet_id[:-1]
            if base not in pairs:
                pairs[base] = []
            pairs[base].append(sheet_id)
        else:
            # Standalone sheet
            if sheet_id not in pairs:
                pairs[sheet_id] = [sheet_id]
    
    return pairs


def validate_brd_anchors(brd_content: str, sheet_ids: list) -> dict:
    """
    Validate that the BRD has proper title-based anchors and links.
    
    Returns:
        Dictionary with validation results
    """
    import re
    
    results = {
        'headings_found': [],
        'anchors_generated': [],
        'links_found': [],
        'broken_links': [],
        'invalid_syntax': []
    }
    
    # Find all markdown headings (## or ### or ####)
    heading_pattern = r'^(#{2,4})\s+(.+?)(?:\s*\{#[^}]+\})*\s*$'
    for match in re.finditer(heading_pattern, brd_content, re.MULTILINE):
        heading_text = match.group(2).strip()
        # Remove any {#id} syntax if present (shouldn't be, but clean up)
        heading_text = re.sub(r'\s*\{#[^}]+\}', '', heading_text)
        results['headings_found'].append(heading_text)
        
        # Generate the anchor that Markdown would create
        anchor = heading_text.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)  # Remove special chars except hyphens
        anchor = re.sub(r'\s+', '-', anchor)  # Replace spaces with hyphens
        anchor = re.sub(r'-+', '-', anchor)  # Collapse multiple hyphens
        anchor = anchor.strip('-')
        results['anchors_generated'].append(anchor)
    
    # Find all internal links: [text](#anchor)
    link_pattern = r'\[([^\]]+)\]\(#([^)]+)\)'
    links = re.findall(link_pattern, brd_content)
    results['links_found'] = [link[1] for link in links]
    
    # Find invalid {#id} syntax in headers (should not exist)
    invalid_pattern = r'^#{2,4}.*\{#[^}]+\}'
    results['invalid_syntax'] = re.findall(invalid_pattern, brd_content, re.MULTILINE)
    
    # Check for broken links (links without matching anchors)
    anchor_set = set(results['anchors_generated'])
    for link_target in results['links_found']:
        if link_target not in anchor_set:
            results['broken_links'].append(link_target)
    
    return results


def synthesize_brd(client: Anthropic, summaries: dict, max_tokens: int = 32000) -> str:
    """
    Use Claude API to synthesize all summaries into a final BRD.
    Uses streaming to handle long-running requests.
    
    Returns:
        Complete BRD in Markdown format
    """
    if not summaries:
        return "# Error\n\nNo summaries provided for synthesis."
    
    # Combine all summaries
    summaries_text = combine_summaries(summaries)
    sheet_ids = extract_sheet_ids(summaries)
    pairs = identify_sheet_pairs(sheet_ids)
    
    # Create user prompt
    user_prompt = USER_PROMPT_TEMPLATE.format(
        num_sheets=len(summaries),
        summaries=summaries_text
    )
    
    print(f"Synthesizing {len(summaries)} sheet summaries into BRD...")
    print(f"Sheet IDs: {sheet_ids}")
    print(f"Identified pairs: {pairs}")
    print(f"Input size: {len(summaries_text):,} characters")
    print(f"Using Claude Sonnet 4.5 with max_tokens={max_tokens}")
    print("-" * 60)
    print("\nGenerating BRD (streaming)...", flush=True)
    
    try:
        # Use streaming for long-running requests
        brd_content = ""
        
        with client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=max_tokens,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        ) as stream:
            for text in stream.text_stream:
                brd_content += text
                # Print progress indicator
                print(".", end="", flush=True)
        
        print(" Done!")
        
        # Validate anchors and links
        print("\nValidating internal links...")
        validation = validate_brd_anchors(brd_content, sheet_ids)
        
        print(f"  Headings found: {len(validation['headings_found'])}")
        print(f"  Auto-generated anchors: {len(validation['anchors_generated'])}")
        print(f"  Internal links found: {len(validation['links_found'])}")
        
        if validation['invalid_syntax']:
            print(f"  ⚠️  Invalid {{#id}} syntax found in {len(validation['invalid_syntax'])} headers")
        
        if validation['broken_links']:
            unique_broken = set(validation['broken_links'])
            print(f"  ⚠️  Broken links ({len(unique_broken)} unique): {list(unique_broken)[:10]}")
            
            # Attempt to auto-fix broken links
            brd_content = fix_broken_links(brd_content, validation)
            
            # Re-validate after fixes
            validation_after = validate_brd_anchors(brd_content, sheet_ids)
            remaining_broken = set(validation_after.get('broken_links', []))
            if remaining_broken:
                print(f"  ⚠️  Remaining broken links after fix: {remaining_broken}")
            else:
                print(f"  ✅ All broken links fixed!")
        
        # Add generation metadata at the end
        metadata = f"\n\n---\n\n*Generated by Claude Sonnet 4.5 from {len(summaries)} sheet summaries*\n"
        metadata += f"*Headings: {len(validation['headings_found'])} | Internal Links: {len(validation['links_found'])}*\n"
        
        # Check final validation state
        final_validation = validate_brd_anchors(brd_content, sheet_ids)
        if final_validation.get('broken_links') or validation.get('invalid_syntax'):
            metadata += f"\n*⚠️ Validation warnings - some links may need manual review*\n"
        else:
            metadata += f"\n*✅ All internal links validated successfully*\n"
        
        brd_content += metadata
        
        return brd_content
        
    except Exception as e:
        error_msg = f"# Error Generating BRD\n\n{str(e)}"
        return error_msg


def post_process_links(brd_content: str) -> str:
    """
    Post-process the BRD to fix common link format issues.
    
    Fixes:
    - Arrow-style links: [text](→target) -> [text](#target)
    - Double hyphens in anchors: (#some--anchor) -> (#some-anchor)
    - Trailing/leading hyphens: (#-anchor-) -> (#anchor)
    """
    import re
    
    # Fix arrow-style links: [text](→target) or [text](-> target)
    brd_content = re.sub(r'\]\(→\s*', '](#', brd_content)
    brd_content = re.sub(r'\]\(->\s*', '](#', brd_content)
    
    # Fix double (or more) hyphens in anchor links: (#some--anchor) -> (#some-anchor)
    def fix_anchor_hyphens(match):
        prefix = match.group(1)  # [text](
        anchor = match.group(2)   # #some--anchor
        # Collapse multiple hyphens to single
        anchor = re.sub(r'-+', '-', anchor)
        # Remove leading/trailing hyphens after #
        anchor = re.sub(r'#-+', '#', anchor)
        anchor = re.sub(r'-+\)', ')', anchor)
        return prefix + anchor + ')'
    
    brd_content = re.sub(r'(\[[^\]]+\]\()([^)]+)(\))', 
                         lambda m: m.group(1) + re.sub(r'-+', '-', m.group(2)).strip('-') + m.group(3), 
                         brd_content)
    
    return brd_content


def fix_broken_links(brd_content: str, validation_results: dict) -> str:
    """
    Attempt to fix broken links by finding the closest matching anchor.
    
    Uses fuzzy matching to find the best anchor for broken links.
    """
    import re
    from difflib import get_close_matches
    
    if not validation_results.get('broken_links'):
        return brd_content
    
    anchors = validation_results.get('anchors_generated', [])
    broken = set(validation_results.get('broken_links', []))
    
    fixes_applied = {}
    
    for broken_link in broken:
        # Try to find a close match
        # First, normalize the broken link (collapse hyphens)
        normalized = re.sub(r'-+', '-', broken_link).strip('-')
        
        # Check if normalized version exists
        if normalized in anchors and normalized != broken_link:
            fixes_applied[broken_link] = normalized
            continue
        
        # Try fuzzy matching
        matches = get_close_matches(normalized, anchors, n=1, cutoff=0.8)
        if matches:
            fixes_applied[broken_link] = matches[0]
    
    # Apply fixes
    for old_link, new_link in fixes_applied.items():
        # Replace in markdown links: [text](#old_link) -> [text](#new_link)
        brd_content = brd_content.replace(f'](#{old_link})', f'](#{new_link})')
    
    if fixes_applied:
        print(f"  🔧 Auto-fixed {len(fixes_applied)} broken links:")
        for old, new in fixes_applied.items():
            print(f"      {old} → {new}")
    
    return brd_content


def main():
    parser = argparse.ArgumentParser(
        description="Synthesize sheet summaries into a final BRD",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        'summaries_dir',
        help='Directory containing sheet summary markdown files'
    )
    
    parser.add_argument(
        'output_file',
        help='Output path for final BRD markdown file'
    )
    
    parser.add_argument(
        '--api-key',
        help='Anthropic API key (uses .env file or ANTHROPIC_API_KEY env var if not provided)'
    )
    
    parser.add_argument(
        '--max-tokens',
        type=int,
        default=32000,
        help='Maximum tokens for Claude response (default: 32000)'
    )
    
    parser.add_argument(
        '--skip-post-process',
        action='store_true',
        help='Skip post-processing link fixes'
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.summaries_dir):
        print(f"Error: Summaries directory not found: {args.summaries_dir}")
        sys.exit(1)
    
    # Check for API key
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: No API key provided.")
        print("Please either:")
        print("  1. Create a .env file with: ANTHROPIC_API_KEY=sk-ant-...")
        print("  2. Set ANTHROPIC_API_KEY environment variable")
        print("  3. Use --api-key argument")
        sys.exit(1)
    
    print(f"Summaries dir: {args.summaries_dir}")
    print(f"Output file: {args.output_file}")
    print(f"Model: Claude Sonnet 4.5")
    print("=" * 60)
    
    # Initialize Anthropic client
    client = Anthropic(api_key=api_key)
    
    # Load all summaries
    print("Loading summaries...", end=" ", flush=True)
    summaries = load_all_summaries(args.summaries_dir)
    print(f"✓ ({len(summaries)} sheets)")
    
    if not summaries:
        print("Error: No summaries found in directory")
        sys.exit(1)
    
    # Synthesize BRD
    brd_content = synthesize_brd(client, summaries, args.max_tokens)
    
    # Post-process to fix any remaining link issues
    if not args.skip_post_process:
        print("\nPost-processing links...", end=" ", flush=True)
        brd_content = post_process_links(brd_content)
        print("✓")
    
    # Write output
    print("Writing BRD...", end=" ", flush=True)
    output_dir = os.path.dirname(args.output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(brd_content)
    
    file_size = os.path.getsize(args.output_file)
    print(f"✓ ({file_size:,} bytes)")
    
    print("=" * 60)
    print(f"✅ BRD synthesis complete")
    print(f"   Output: {args.output_file}")
    print(f"   Size: {file_size:,} bytes")


if __name__ == "__main__":
    main()