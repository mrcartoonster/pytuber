# -*- coding: utf-8 -*-
from typing import List

import typer
from typing_extensions import Annotated
from youtube_func import youtube


def main(video: List[Annotated[str, typer.Argument()]]):
    """
    Simple pytube.
    """
    for _ in video:
        youtube(_)


if __name__ == "__main__":
    typer.run(main)
