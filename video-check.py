# pip install pymediainfo

import os
import subprocess
import time
import shutil
from pymediainfo import MediaInfo

VLC = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'
TYPE = '.mkv'

PATH = "F:\\Seasons\\__corrupted\\Discovery_Channel"
FILE = 'F:\\Movies\\english-br\\Action\\DRIVE ANGRY\\part 1.mkv'

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
    DST = 'F:\\Seasons\\2_get\\'
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all subdirectories first.
        for dir in dirnames:
            for file in os.listdir(os.path.join(path,dir)):
                if file.endswith('get.txt'):
                    move = True
            if move:        
                print "Moving " + os.path.join(path,dir)         
                shutil.move(os.path.join(path,dir), DST)
                move = False
        break    

def playFilesDir(path):
    for file in os.listdir(path):
        if not file.endswith(TYPE):
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
            if vid.endswith(TYPE):
                print dir
                time.sleep(2)
                p = subprocess.Popen([VLC, vid, '--start-time', str(5400)])
                time.sleep(8)
                p.kill()                     