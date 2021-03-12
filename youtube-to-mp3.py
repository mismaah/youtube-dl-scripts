"""
Download as mp3 format with the video thumbnail embeded.
"""

import subprocess

while True:
    url = input("Enter youtube url: ")
    subprocess.run(
        f'youtube-dl {url} -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --postprocessor-args "-id3v2_version 3"'
    )
