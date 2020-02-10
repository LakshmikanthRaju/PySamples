#!/usr/bin/env python

# Run all the video files in given folder at regular periods to check if it is corrupted
#
# Command line inputs: None
# Runtime inputs: None

import os
import random
import subprocess

VLC = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
VIDEO_TYPES = ['.mkv', '.avi', '.mp4']

def isVideo(f):
    if f.endswith('.avi') or f.endswith('.mkv') or f.endswith('.mp4') :
        return True
    return False

def getPlayRandomEpisode(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    rand_num = random.randint(0, len(dirs)-1)
    rand_dir = os.path.join(path,dirs[rand_num])

    files = [f for f in os.listdir(rand_dir) if os.path.isfile(os.path.join(rand_dir, f)) and isVideo(f)]
    rand_num = random.randint(0, len(files)-1)
    p = subprocess.Popen([VLC, os.path.join(rand_dir, files[rand_num])])

if __name__ == "__main__":
    getPlayRandomEpisode(os.getcwd())