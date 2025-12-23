import os
import sys
import argparse
from dotenv import load_dotenv
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Initialize Rich Console
console = Console()

def get_api_key():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        # Fallback to check if user kept the old variable name
        api_key = os.getenv("OPENAI_API_KEY")
        
    if not api_key:
        console.print("[bold red]Error:[/bold red] GEMINI_API_KEY (or OPENAI_API_KEY) not found in environment variables.")
        console.print("Please create a .env file and add your API Key.")
        sys.exit(1)
    return api_key

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Could not read file: {e}")
        sys.exit(1)

def review_code(file_path):
    api_key = get_api_key()
    code_content = read_file(file_path)
    
    # Configure Gemini
    genai.configure(api_key=api_key)
    
    # Initialize Model
    model = genai.GenerativeModel('gemini-pro')
    
    console.print(f"[bold blue]🚀 Starting Senior Code Review for:[/bold blue] [yellow]{file_path}[/yellow]")
    console.print("[dim]Analyzing code structure, logic, and style (Powered by Gemini 💎)...[/dim]\n")

    try:
        # Construct the prompt manually since Gemini doesn't strictly separate system/user the same way in all versions,
        # but modern usage supports system instruction or just prepending.
        # Ideally using system_instruction in GenerativeModel init if supported, but prepending is safe.
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser Code:\n```\n{code_content}\n```"

        response = model.generate_content(full_prompt, stream=True)

        collected_content = ""
        
        # Live streaming output
        with Live(console=console, refresh_per_second=10) as live:
            for chunk in response:
                if chunk.text:
                    collected_content += chunk.text
                    live.update(Markdown(collected_content))

    except Exception as e:
        console.print(f"\n[bold red]API Error:[/bold red] {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Powered Senior Code Reviewer CLI (Gemini Edition)")
    parser.add_argument("file", help="Path to the file you want to review")
    args = parser.parse_args()

    review_code(args.file)
