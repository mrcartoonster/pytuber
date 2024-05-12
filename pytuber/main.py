# -*- coding: utf-8 -*-
from typing import List

import typer
from typing_extensions import Annotated
from youtube_func import youtube

app = typer.Typer()


@app.command()
def url(video: List[Annotated[str, typer.Argument()]]):
    """
    Simple pytube.
    """
    for _ in video:
        youtube(_)


if __name__ == "__main__":
    app()
