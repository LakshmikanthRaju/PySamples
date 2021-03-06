#!/usr/bin/env python

# Run all the video files in given folder at regular periods to check if it is corrupted
#
# Set up:
#   pip install pymediainfo
#
# Command line inputs: None
# In file inputs:
#   Give folder name in PATH
# Runtime inputs: None

import os
import subprocess
import time
import shutil
from pymediainfo import MediaInfo

PATH = "F:\\Seasons\\__corrupted\\Discovery_Channel"
MOVE_DEST = 'F:\\Seasons\\2_get\\'

VLC = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
VIDEO_TYPES = ['.mkv', '.avi', '.mp4']

def displayDirs(path):
    for dir in os.listdir(path):
        print dir
        
def cutOff():  
    DST = 'F:\\Seasons\\__corrupted\\Discovery_Channel'
    for dirname, dirnames, filenames in os.walk(DST):
        # print path to all subdirectories first.
        for dir in dirnames:
            for file in os.listdir(os.path.join(DST,dir)):
                if file.endswith('.avi') or file.endswith('.mkv') or file.endswith('.mp4') :
                    shutil.move(os.path.join(DST,dir,file), DST)
        
def getDuration(file):
    media_info = MediaInfo.parse('my_video_file.mov')
    duration_in_ms = media_info.tracks[0].duration
    return duration_in_ms/1000
    
def moveDir(path):
    move = False
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all subdirectories first.
        for dir in dirnames:
            for file in os.listdir(os.path.join(path,dir)):
                if file.endswith('get.txt'):
                    move = True
            if move:        
                print "Moving " + os.path.join(path,dir)         
                shutil.move(os.path.join(path,dir), MOVE_DEST)
                move = False
        break    

def playFilesDir(path):
    for file in os.listdir(path):
        file_type = file[file.rfind('.'):]
        if file_type not in file.endswith(VIDEO_TYPES):
            continue
        vid = os.path.join(path, file)
        print file
        time.sleep(1)
        i = 0
        while i < 5:    
            p = subprocess.Popen([VLC, vid, '--start-time', str(120 + (i * 550))])
            time.sleep(5)
            p.kill() 
            i += 1

if __name__ == "__main__":
    #displayDirs(PATH)
    #print os.stat(FILE).st_size
    #FILE = 'F:\\Movies\\english-br\\Action\\DRIVE ANGRY\\part 1.mkv'
    #print FILE
    playFilesDir(PATH)
    #moveDir('F:\Seasons\_updated')
    #cutOff()
    
def playFile(file):
    i = 0
    p = subprocess.Popen([VLC, file])
    time.sleep(5)
    while i < 6:
        time.sleep(5)
        p.kill()
        p = subprocess.Popen([VLC, file, '--start-time', str(600*i)])
        i += 1    
        
def playFiles(path):
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all subdirectories first.
        for dir in dirnames:
            vid = os.path.join(path, dir, os.listdir(os.path.join(path, dir))[0])
            vid_type = vid[vid.rfind('.'):]
            if vid_type in VIDEO_TYPES:
                print dir
                time.sleep(2)
                p = subprocess.Popen([VLC, vid, '--start-time', str(5400)])
                time.sleep(8)
                p.kill()                     