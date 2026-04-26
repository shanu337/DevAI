import typer
from devai.ai import ask_ai
from rich import print
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def explain(file: str):
    with open(file, "r") as f:
        code = f.read()

    prompt = f"Explain this code:\n{code}"

    with console.status("[bold green]Thinking..."):
        response = ask_ai(prompt)

    print(f"[bold green]{response}[/bold green]")


@app.command()
def generate(query: str):
    prompt = f"""
You are an expert programmer.

Task: {query}

Give:
- Clean code
- Short explanation
- Edge cases if important
"""

    with console.status("[bold green]Thinking..."):
        response = ask_ai(prompt)

    print(f"[bold green]{response}[/bold green]")


@app.command()
def fix(error: str):
    prompt = f"Fix this error and explain it: {error}"

    with console.status("[bold green]Thinking..."):
        response = ask_ai(prompt)

    print(f"[bold green]{response}[/bold green]")


@app.command()
def chat(query: str):
    with console.status("[bold green]Thinking..."):
        response = ask_ai(query)

    print(f"[bold green]{response}[/bold green]")


if __name__ == "__main__":
    app()
