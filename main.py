#!/usr/bin/env python3
"""
Complete Excel-to-Markdown Pipeline

Orchestrates the full workflow:
1. Excel → CSV (via excel_converter.py)
2. CSV → Markdown (via csv_md_converter.py)

Usage:
    python main.py <excel_file> [output_md]

Example:
    python main.py data/BRD_input.xlsx final_output.md
    python main.py data/BRD_input.xlsx  # outputs to stdout

Output:
    - Intermediate CSV (temporary, unless --keep-csv is used)
    - Final Markdown file (or stdout)
    - Images directory (from excel_converter.py)
"""

import sys
import os
import tempfile
import subprocess
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...", file=sys.stderr)
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout, file=sys.stderr)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {description} failed", file=sys.stderr)
        if e.stdout:
            print(e.stdout, file=sys.stderr)
        if e.stderr:
            print(e.stderr, file=sys.stderr)
        sys.exit(1)


def excel_to_markdown(excel_path: str, output_md_path: str = None, keep_csv: bool = False) -> str:
    """
    Convert Excel file to Markdown through CSV intermediate.
    
    Args:
        excel_path: Path to input Excel file
        output_md_path: Path to save output Markdown (None = print to stdout)
        keep_csv: If True, keep the intermediate CSV file
        
    Returns:
        Generated Markdown string (if output_md_path is None) or path to output file
    """
    # Validate input
    if not os.path.exists(excel_path):
        print(f"❌ Error: Excel file not found: {excel_path}", file=sys.stderr)
        sys.exit(1)
    
    excel_path = os.path.abspath(excel_path)
    
    # Determine CSV path
    if keep_csv:
        # Save CSV in current directory with same name as output
        if output_md_path:
            csv_path = os.path.splitext(output_md_path)[0] + '.csv'
        else:
            csv_path = os.path.splitext(excel_path)[0] + '.csv'
    else:
        # Use temporary file
        csv_fd, csv_path = tempfile.mkstemp(suffix='.csv')
        os.close(csv_fd)
    
    try:
        # Step 1: Convert Excel to CSV
        print(f"📖 Input Excel:  {excel_path}", file=sys.stderr)
        print(f"📊 Intermediate CSV: {csv_path}", file=sys.stderr)
        
        cmd = [sys.executable, 'excel_converter.py', excel_path, csv_path]
        run_command(cmd, "Converting Excel to CSV")
        
        # Step 2: Convert CSV to Markdown
        if output_md_path:
            print(f"📝 Output MD:    {output_md_path}", file=sys.stderr)
            cmd = [sys.executable, 'csv_md_converter.py', csv_path, output_md_path]
            run_command(cmd, "Converting CSV to Markdown")
            return output_md_path
        else:
            # Output to stdout
            cmd = [sys.executable, 'csv_md_converter.py', csv_path]
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            return result.stdout
    
    finally:
        # Clean up temporary CSV if not keeping it
        if not keep_csv and os.path.exists(csv_path):
            try:
                os.remove(csv_path)
                print(f"🗑️  Cleaned up temporary CSV", file=sys.stderr)
            except Exception as e:
                print(f"⚠️  Warning: Could not remove temporary CSV: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    excel_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    keep_csv = '--keep-csv' in sys.argv
    
    print(f"✨ Excel-to-Markdown Pipeline", file=sys.stderr)
    print(f"{'=' * 50}", file=sys.stderr)
    
    result = excel_to_markdown(excel_file, output_file, keep_csv)
    
    if output_file:
        print(f"{'=' * 50}", file=sys.stderr)
        print(f"✅ Complete! Markdown saved to: {result}", file=sys.stderr)
    else:
        print(result)
