import click
import os
from pathlib import Path

"""
CLI Method
Handles user input and program start up via CLI
"""

@click.command()
@click.argument("path", nargs=-1, type=str, required=True)
def cli(path):

    for item in path:
        item_path = Path(item)
        try:
            """Does user provided filepath exist?"""
            item_path.resolve(strict=True)
        except:
            print("Error: File path provided does not exist")
            raise SystemExit(1)
        else:
            print("File exists")
            """process file"""


if __name__ == '__main__':
    cli()
