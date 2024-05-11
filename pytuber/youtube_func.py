# -*- coding: utf-8 -*-
"""
YouTube function.
"""
from pytube import YouTube


def youtube(video: str):
    """
    Basic youtube function to download a video.
    """
    yt = YouTube(video)

    print(f"Downloading: {yt.title}.")

    yt.streams.get_highest_resolution().download()
