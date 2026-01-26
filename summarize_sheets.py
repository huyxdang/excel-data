"""
Summarize Sheets using Claude API

Analyzes each extracted CSV sheet using Claude Sonnet 4.5 and generates
structured markdown summaries suitable for BRD synthesis.

Usage:
    python summarize_sheets.py <sheets_dir> <output_dir> [--api-key KEY]

Example:
    python summarize_sheets.py output/sheets output/summaries
    python summarize_sheets.py output/sheets output/summaries --api-key sk-ant-...
    
Environment:
    ANTHROPIC_API_KEY - API key for Claude (loaded from .env file or environment)
    
.env file format:
    ANTHROPIC_API_KEY=sk-ant-...
    
Output:
    output/summaries/
    ├── 0.md
    ├── 1.md
    ├── 5.md
    ├── 5.1.1a.md
    └── ...
    output/summaries/_index.md (summary index)
"""

import sys
import os
import csv
import glob
import argparse
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


SUMMARIZATION_PROMPT = """Đọc sheet này từ tài liệu Yêu cầu Nghiệp vụ (BRD) và phân tích nội dung.

Tên sheet: {sheet_name}
Nội dung sheet (định dạng CSV):
{content}

Vui lòng đưa ra:

1. **Loại sheet**: Phân loại là một trong các loại: tổng-quan/quy-trình/giao-diện/đặc-tả/mô-hình-dữ-liệu/khác

2. **Mức độ chi tiết**: Phân loại là một trong hai loại:
   - `chi-tiết-cao`: Sheet chứa nhiều thông số kỹ thuật, số liệu cụ thể, validation rules, field specifications, hoặc data mapping → CẦN GIỮ NGUYÊN DẠNG BẢNG
   - `tổng-quan`: Sheet chứa mô tả quy trình, luồng công việc, hoặc thông tin high-level → CÓ THỂ CHUYỂN THÀNH PROSE/SECTIONS

3. **Chủ đề/tiêu đề chính**: Chủ đề hoặc mục đích chính của sheet này là gì?

4. **Tóm tắt thông tin chính**: Cung cấp 2-3 đoạn văn tóm tắt các thông tin thiết yếu, logic nghiệp vụ và yêu cầu trong sheet này.

5. **Các bên liên quan/vai trò được đề cập**: Liệt kê các cá nhân, nhóm, vai trò hoặc phòng ban được đề cập.

6. **Các yêu cầu tìm thấy**: Trích xuất các yêu cầu, đặc tả hoặc ràng buộc rõ ràng (nếu có).

7. **Các sheet liên quan**: Xác định các tham chiếu đến sheet khác, tài liệu hoặc hệ thống khác.

8. **Bảng cần giữ nguyên** (CHỈ khi mức độ chi tiết = `chi-tiết-cao`):
   Nếu sheet chứa bảng với thông số kỹ thuật quan trọng, hãy chuyển đổi sang định dạng Markdown table và đưa vào đây.
   
   Các loại bảng CẦN giữ nguyên:
   - Bảng field specifications (tên trường, kiểu dữ liệu, độ dài, bắt buộc/không)
   - Bảng validation rules
   - Bảng status/state transitions
   - Bảng data mapping (source → target)
   - Bảng API specifications
   - Bảng error codes
   - Bảng permission/role matrix
   
   Định dạng Markdown table:
   ```markdown
   | Tên trường | Kiểu dữ liệu | Độ dài | Bắt buộc | Mô tả |
   |------------|--------------|--------|----------|-------|
   | ma_yeu_cau | VARCHAR      | 50     | Có       | Mã yêu cầu theo format NK.YY.xxxx |
   ```

Trình bày phân tích của bạn dưới dạng markdown ngôn ngữ tự nhiên (KHÔNG phải JSON). Ngắn gọn nhưng đầy đủ."""


def load_csv_content(csv_path: str, max_rows: int = 500) -> tuple[str, int]:
    """
    Load CSV content as text, limited to max_rows.
    
    Returns:
        (content_text, total_row_count)
    """
    rows = []
    total_rows = 0
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                total_rows += 1
                if i < max_rows:
                    rows.append(','.join(row))
                    
        content = '\n'.join(rows)
        
        if total_rows > max_rows:
            content += f"\n\n... ({total_rows - max_rows} more rows truncated)"
            
        return content, total_rows
        
    except Exception as e:
        print(f"Error reading {csv_path}: {e}")
        return "", 0


def summarize_sheet(client: Anthropic, sheet_name: str, csv_path: str, max_tokens: int = 2000) -> str:
    """
    Use Claude API to summarize a single sheet.
    
    Returns:
        Markdown summary text
    """
    content, row_count = load_csv_content(csv_path)
    
    if not content:
        return f"# {sheet_name}\n\n*Error: Could not read sheet content*"
    
    prompt = SUMMARIZATION_PROMPT.format(
        sheet_name=sheet_name,
        content=content
    )
    
    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        summary = message.content[0].text
        
        # Add metadata footer
        summary += f"\n\n---\n*Source: {sheet_name}.csv | Rows: {row_count} | Generated by Claude Sonnet 4.5*\n"
        
        return summary
        
    except Exception as e:
        error_msg = f"# {sheet_name}\n\n*Error generating summary: {e}*"
        return error_msg


def get_sheet_name_from_filename(filename: str) -> str:
    """
    Extract sheet name from CSV filename.
    
    Examples:
        '5.1.1a.csv' -> '5.1.1a'
        'Status.csv' -> 'Status'
    """
    return os.path.splitext(os.path.basename(filename))[0]


def summarize_all_sheets(sheets_dir: str, output_dir: str, api_key: str = None) -> dict:
    """
    Summarize all CSV sheets in the directory.
    
    Args:
        sheets_dir: Directory containing CSV files
        output_dir: Directory to save markdown summaries
        api_key: Optional API key (uses env var if not provided)
        
    Returns:
        Dictionary with summarization results
    """
    # Initialize Anthropic client
    client = Anthropic(api_key=api_key) if api_key else Anthropic()
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all CSV files
    csv_files = sorted(glob.glob(os.path.join(sheets_dir, "*.csv")))
    
    if not csv_files:
        print(f"No CSV files found in {sheets_dir}")
        return {'success': [], 'failed': []}
    
    print(f"Found {len(csv_files)} CSV files")
    print("-" * 60)
    
    results = {
        'success': [],
        'failed': [],
        'summaries': {}
    }
    
    for i, csv_path in enumerate(csv_files):
        sheet_name = get_sheet_name_from_filename(csv_path)
        output_md = os.path.join(output_dir, f"{sheet_name}.md")
        
        print(f"[{i+1}/{len(csv_files)}] Summarizing '{sheet_name}'...", end=" ", flush=True)
        
        try:
            summary = summarize_sheet(client, sheet_name, csv_path)
            
            # Write summary to file
            with open(output_md, 'w', encoding='utf-8') as f:
                f.write(summary)
            
            file_size = os.path.getsize(output_md)
            print(f"✓ ({file_size:,} bytes)")
            
            results['success'].append(sheet_name)
            results['summaries'][sheet_name] = {
                'csv_path': csv_path,
                'md_path': output_md,
                'size': file_size
            }
            
        except Exception as e:
            print(f"✗ {e}")
            results['failed'].append(sheet_name)
    
    # Create index file
    create_index(results, output_dir)
    
    return results


def create_index(results: dict, output_dir: str):
    """Create an index markdown file listing all summaries."""
    index_path = os.path.join(output_dir, "_index.md")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Sheet Summaries Index\n\n")
        f.write(f"Total sheets: {len(results['success']) + len(results['failed'])}\n")
        f.write(f"- Successfully summarized: {len(results['success'])}\n")
        f.write(f"- Failed: {len(results['failed'])}\n\n")
        
        if results['success']:
            f.write("## Summaries\n\n")
            for sheet_name in sorted(results['success']):
                info = results['summaries'][sheet_name]
                f.write(f"- [{sheet_name}](./{sheet_name}.md) ({info['size']:,} bytes)\n")
        
        if results['failed']:
            f.write("\n## Failed\n\n")
            for sheet_name in results['failed']:
                f.write(f"- {sheet_name}\n")
    
    print(f"\n📄 Index created: {index_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Summarize Excel sheets using Claude API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        'sheets_dir',
        help='Directory containing CSV sheet files'
    )
    
    parser.add_argument(
        'output_dir',
        help='Directory to save markdown summaries'
    )
    
    parser.add_argument(
        '--api-key',
        help='Anthropic API key (uses .env file or ANTHROPIC_API_KEY env var if not provided)'
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.sheets_dir):
        print(f"Error: Sheets directory not found: {args.sheets_dir}")
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
    
    print(f"Sheets dir: {args.sheets_dir}")
    print(f"Output dir: {args.output_dir}")
    print(f"Model: Claude Sonnet 4.5")
    print("=" * 60)
    
    results = summarize_all_sheets(args.sheets_dir, args.output_dir, api_key)
    
    print("=" * 60)
    print(f"✅ Summarization complete")
    print(f"   Success: {len(results['success'])} sheets")
    print(f"   Failed:  {len(results['failed'])} sheets")
    print(f"   Output:  {args.output_dir}/")
    
    if results['failed']:
        print(f"\n⚠️  Failed sheets: {results['failed']}")


if __name__ == "__main__":
    main()