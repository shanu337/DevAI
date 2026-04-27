import typer
import pyperclip
import time
from devai.ai import ask_ai
from rich.console import Console

app = typer.Typer(help="DevAI 😈 - AI coding assistant in your terminal")
console = Console()


def display_response(response: str):
    console.print("\n[bold green]✨ Response:[/bold green]\n")

    # typing effect 😈
    for char in response:
        print(char, end="", flush=True)
        time.sleep(0.003)
    print()

    console.print("\n[green]✅ Done![/green]")


@app.command(help="Explain a code file")
def explain(file: str, copy: bool = False, save: str = None):
    try:
        with open(file, "r") as f:
            code = f.read()

        prompt = f"Explain this code:\n{code}"

        with console.status("[bold green]Thinking..."):
            response = ask_ai(prompt)

        display_response(response)

        if copy:
            pyperclip.copy(response)
            console.print("[yellow]📋 Copied to clipboard![/yellow]")

        if save:
            with open(save, "w") as f:
                f.write(response)
            console.print(f"[cyan]💾 Saved to {save}[/cyan]")

    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command(help="Generate clean code from a prompt")
def generate(query: str, copy: bool = False, save: str = None):
    prompt = f"""
You are an expert programmer.

Task: {query}

Give:
- Clean code
- Short explanation
- Edge cases if important
"""

    try:
        with console.status("[bold green]Thinking..."):
            response = ask_ai(prompt)

        display_response(response)

        if copy:
            pyperclip.copy(response)
            console.print("[yellow]📋 Copied to clipboard![/yellow]")

        if save:
            with open(save, "w") as f:
                f.write(response)
            console.print(f"[cyan]💾 Saved to {save}[/cyan]")

    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command(help="Fix an error and explain it")
def fix(error: str, copy: bool = False, save: str = None):
    prompt = f"Fix this error and explain it: {error}"

    try:
        with console.status("[bold green]Thinking..."):
            response = ask_ai(prompt)

        display_response(response)

        if copy:
            pyperclip.copy(response)
            console.print("[yellow]📋 Copied to clipboard![/yellow]")

        if save:
            with open(save, "w") as f:
                f.write(response)
            console.print(f"[cyan]💾 Saved to {save}[/cyan]")

    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command(help="Chat with AI")
def chat(query: str, copy: bool = False, save: str = None):
    try:
        with console.status("[bold green]Thinking..."):
            response = ask_ai(query)

        display_response(response)

        if copy:
            pyperclip.copy(response)
            console.print("[yellow]📋 Copied to clipboard![/yellow]")

        if save:
            with open(save, "w") as f:
                f.write(response)
            console.print(f"[cyan]💾 Saved to {save}[/cyan]")

    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


# ⚡ SHORTCUT COMMANDS (power users 😈)
@app.command()
def g(query: str):
    generate(query)


@app.command()
def f(error: str):
    fix(error)


@app.command()
def e(file: str):
    explain(file)


@app.command()
def c(query: str):
    chat(query)


if __name__ == "__main__":
    app()
