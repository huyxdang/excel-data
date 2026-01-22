import sys
import os
import time
from dotenv import load_dotenv
import anthropic
import csv
from io import StringIO

# Load environment variables from .env file
load_dotenv()

"""
CSV to Markdown Converter using Claude API
Reads a CSV file (from excel_converter.py output) and uses Claude Sonnet 4.5
to generate a deterministic Markdown file following the rules in prompt.md.

Usage:
    python csv_md_converter.py <input_csv> [output_md]

Example:
    python csv_md_converter.py output.csv final_output.md
"""

# Approximate tokens per row (adjust based on your data)
MAX_ROWS_PER_CHUNK = 50  # Start conservative, adjust as needed


def read_file(file_path: str) -> str:
    """Read file content."""
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def load_prompt() -> str:
    """Load the system prompt from prompt.md."""
    prompt_path = os.path.join(os.path.dirname(__file__), 'prompt.md')
    if not os.path.exists(prompt_path):
        print(f"Error: prompt.md not found at {prompt_path}")
        sys.exit(1)
    return read_file(prompt_path)


def split_csv_into_chunks(csv_content: str, max_rows: int = MAX_ROWS_PER_CHUNK) -> list[tuple[str, str]]:
    """
    Split CSV into chunks, preserving headers.
    
    Returns:
        List of (chunk_csv_string, row_info) tuples
    """
    reader = csv.reader(StringIO(csv_content))
    rows = list(reader)
    
    if len(rows) <= 1:
        return [(csv_content, "all rows")]
    
    header = rows[0]
    data_rows = rows[1:]
    
    chunks = []
    for i in range(0, len(data_rows), max_rows):
        chunk_rows = data_rows[i:i + max_rows]
        
        # Reconstruct CSV with header
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(header)
        writer.writerows(chunk_rows)
        
        chunk_csv = output.getvalue()
        row_range = f"rows {i+1}-{min(i+max_rows, len(data_rows))} of {len(data_rows)}"
        chunks.append((chunk_csv, row_range))
    
    return chunks


def format_duration(seconds: float) -> str:
    """Format duration in human-readable format."""
    if seconds < 60:
        return f"{seconds:.2f}s"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}m {secs:.2f}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hours}h {minutes}m {secs:.2f}s"


def convert_chunk_to_markdown(client: anthropic.Anthropic, system_prompt: str, 
                              csv_chunk: str, chunk_info: str, is_continuation: bool = False) -> tuple[str, float, dict]:
    """
    Convert a single CSV chunk to Markdown.
    
    Returns:
        Tuple of (markdown_content, latency_seconds, usage_stats)
    """
    
    if is_continuation:
        user_message = f"""Continue converting the CSV to Markdown. This is {chunk_info}.
Do NOT include the document header again, just continue with the content rows.

CSV chunk:
{csv_chunk}"""
    else:
        user_message = f"""Convert the following CSV to Markdown. This is {chunk_info}.

{csv_chunk}"""
    
    start_time = time.time()
    
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=16000,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    
    latency = time.time() - start_time
    
    usage_stats = {
        "input_tokens": message.usage.input_tokens,
        "output_tokens": message.usage.output_tokens,
    }
    
    return message.content[0].text, latency, usage_stats


def convert_csv_to_markdown(csv_path: str, output_md_path: str = None) -> str:
    """
    Convert CSV file to Markdown using Claude API with chunking.
    """
    total_start_time = time.time()
    
    # Read input CSV
    csv_content = read_file(csv_path)
    
    # Load system prompt
    system_prompt = load_prompt()
    
    # Initialize Anthropic client
    client = anthropic.Anthropic()
    
    # Split CSV into chunks
    chunks = split_csv_into_chunks(csv_content)
    total_chunks = len(chunks)
    
    print(f"📊 CSV split into {total_chunks} chunk(s)", file=sys.stderr)
    print(f"{'─' * 60}", file=sys.stderr)
    
    markdown_parts = []
    chunk_latencies = []
    total_input_tokens = 0
    total_output_tokens = 0
    
    for i, (chunk_csv, chunk_info) in enumerate(chunks):
        print(f"🔄 Processing chunk {i+1}/{total_chunks} ({chunk_info})...", file=sys.stderr, end=" ")
        
        is_continuation = i > 0
        markdown_part, latency, usage = convert_chunk_to_markdown(
            client, system_prompt, chunk_csv, chunk_info, is_continuation
        )
        
        markdown_parts.append(markdown_part)
        chunk_latencies.append(latency)
        total_input_tokens += usage["input_tokens"]
        total_output_tokens += usage["output_tokens"]
        
        print(f"✓ {format_duration(latency)} ({usage['input_tokens']:,} in / {usage['output_tokens']:,} out)", file=sys.stderr)
    
    # Combine all parts
    markdown_content = "\n\n".join(markdown_parts)
    
    # Calculate statistics
    total_time = time.time() - total_start_time
    avg_latency = sum(chunk_latencies) / len(chunk_latencies) if chunk_latencies else 0
    
    # Print summary
    print(f"{'─' * 60}", file=sys.stderr)
    print(f"📈 SUMMARY", file=sys.stderr)
    print(f"   Total time:      {format_duration(total_time)}", file=sys.stderr)
    print(f"   Avg per chunk:   {format_duration(avg_latency)}", file=sys.stderr)
    print(f"   Min chunk time:  {format_duration(min(chunk_latencies))}", file=sys.stderr)
    print(f"   Max chunk time:  {format_duration(max(chunk_latencies))}", file=sys.stderr)
    print(f"   Total tokens:    {total_input_tokens + total_output_tokens:,} ({total_input_tokens:,} in / {total_output_tokens:,} out)", file=sys.stderr)
    print(f"{'─' * 60}", file=sys.stderr)
    
    # Save or print output
    if output_md_path:
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"✅ Markdown saved to: {output_md_path}", file=sys.stderr)
    else:
        print(markdown_content)
    
    return markdown_content


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    csv_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"📖 Input CSV:  {csv_file}", file=sys.stderr)
    if output_file:
        print(f"📝 Output MD:  {output_file}", file=sys.stderr)
    
    convert_csv_to_markdown(csv_file, output_file)