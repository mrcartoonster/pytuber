# -*- coding: utf-8 -*-
import typer
from rich import print

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(
            f"[bold green]Awesome Pytuber CLI version:[/] [purple link=https://bit.ly/3yeuVCy]{__version__}[/]",
        )

        raise typer.Exit()
