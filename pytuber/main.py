# -*- coding: utf-8 -*-
from pathlib import Path
from typing import List, Optional

import typer
from rich import print
from rich.progress import track
from typer_funcs import version_callback
from typing_extensions import Annotated
from youtube_func import youtube, youtube_listing

app = typer.Typer(no_args_is_help=True, add_completion=False)


@app.command()
def url(
    # Video URL(s)
    video: List[Annotated[str, typer.Argument()]],
    # Directory option parameter
    target: Annotated[
        Optional[Path],
        typer.Option(
            "--target",
            "-t",
            help="The output directory for the downloaded stream. Default is current working directory.",
        ),
    ] = None,
    # Print downloadable streams
    listing: Annotated[
        Optional[bool],
        typer.Option(
            "--list",
            "-l",
            help="The list option causes pytuber cli to return a list of streams available to download.",
        ),
    ] = None,
    # Print CLI version
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            callback=version_callback,
            is_eager=True,
            help="Show programs version and exit. You can click on version to go to GitHub Repo.",
        ),
    ] = None,
):
    """
    Command line application to download youtube videos.
    """
    if target:
        for _ in track(video, description="Processing..."):
            youtube(_, target=target)

    elif listing:
        try:
            youtube_listing(*video)
        except TypeError:
            print(
                "[red]Can only pass one YouTube url to get a list of streams.[/]",
            )

    else:
        for _ in track(video, description="Processing..."):
            youtube(_)


if __name__ == "__main__":
    app()
