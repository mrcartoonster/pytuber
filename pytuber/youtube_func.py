# -*- coding: utf-8 -*-
"""
YouTube function.
"""
from pathlib import Path
from typing import Optional

from pytube import YouTube
from rich import print


def youtube(video: str, target: Optional[Path] = None):
    """
    Basic YouTube function to download a video.
    """
    yt = YouTube(video)

    print("[green]Loading video[/]")

    print(f"Downloading: [underline]{yt.title}[/]")

    yt.streams.get_highest_resolution().download(output_path=target)


def youtube_listing(video_list: str):
    """
    Output a list of YouTube streams for download.
    """
    yt = YouTube(video_list)

    print("[turquoise4]Generating list of downloadable streams...[/]")
    print(f"[bold]{yt.title}[/]")

    stream_list = [_ for _ in yt.streams]

    for _ in stream_list:
        print(_)
