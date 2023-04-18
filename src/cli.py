import typer
import sim

app = typer.Typer()

@app.command()
def run(file: str):
    with open(file, "r") as f:
        simfile = sim.Lang(f.readlines())
        simfile.parse_lines()

app()