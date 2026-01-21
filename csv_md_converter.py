import sys
import os
from dotenv import load_dotenv
import anthropic

# Load environment variables from .env file
load_dotenv()

"""
CSV to Markdown Converter using Claude API

Reads a CSV file (from excel_converter.py output) and uses Claude Sonnet 3.5
to generate a deterministic Markdown file following the rules in prompt.md.

Usage:
    python csv_md_converter.py <input_csv> [output_md]

Example:
    python csv_md_converter.py output.csv final_output.md
"""



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


def convert_csv_to_markdown(csv_path: str, output_md_path: str = None) -> str:
    """
    Convert CSV file to Markdown using Claude API.
    
    Args:
        csv_path: Path to input CSV file
        output_md_path: Path to save output Markdown (None = print to stdout)
        
    Returns:
        Generated Markdown string
    """
    # Read input CSV
    csv_content = read_file(csv_path)
    
    # Load system prompt
    system_prompt = load_prompt()
    
    # Initialize Anthropic client
    client = anthropic.Anthropic()
    
    # Call Claude API
    print("🔄 Sending to Claude Sonnet 3.5...", file=sys.stderr)
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=16000,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"Convert the following CSV to Markdown:\n\n{csv_content}"
            }
        ]
    )
    
    markdown_content = message.content[0].text
    
    # Save or print output
    if output_md_path:
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"✅ Markdown saved to: {output_md_path}")
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