#!/usr/bin/env python

# Renames subtitles to video's name to support automatic subtitle loading
# Removes unwanted sample videos, zip files and images
# Clubs videos of same series together for easy access
#
# Set up: None
#
# Command line inputs: None
# In file inputs:
#   Give folder name in SRC_DIR
#   Give currency code in CURRENCY url
# Runtime inputs: None


import os
import sys
import shutil

SRC_DIR = 'F:\\Enters'

VIDEO_TYPES = ['.mp4','.avi','.mkv','.vob','.flv','.rmvb','.mpg']
DEL_FILES = ['.txt','.zip','.nfo','.db','.jpg','.png','.rar']
SUBS_TYPE = ['.srt']
SUB_SRT = ".srt"
THRESHHOLD = 7
#checkPoint = 17

def getVideoFilesCount(dir):
    count = 0
    for f in os.listdir(dir):
        pos = f.rfind('.')
        type = f[pos:]
        
        if type in VIDEO_TYPES:
            count = count + 1
            
    return count
    
def getSubtitleFilesCount(dir):
    count = 0
    for s in os.listdir(dir):
        if s.endswith(SUB_SRT):
            count = count + 1
    return count
    
def renameSingleVideoSubtitle(dir):
    name = ""
    sub = ""
    
    for f in os.listdir(dir):        
        pos = f.rfind('.')
        type = f[pos:]
        if type in DEL_FILES:
            os.remove(os.path.join(dir,f))
        elif type in VIDEO_TYPES:
            name = f[:pos]
        elif f.endswith(SUB_SRT):
            sub = f
    
    if name and sub:
        subName = name+SUB_SRT
        if sub != subName:
            if os.path.exists(os.path.join(dir,subName)):
                os.remove(os.path.join(dir,sub))
            try:
                os.rename(os.path.join(dir,sub), os.path.join(dir,subName))        
            except WindowsError as err:
                print err, os.path.join(dir,sub)
    return
                
    
def processRecursiveSingleVideos(dirFolder):
    for root, directories, filenames in os.walk(dirFolder):
        for dir in directories:
            if getVideoFilesCount(os.path.join(root,dir)) == 1:
                print os.path.join(root,dir)
                renameSingleVideoSubtitle(os.path.join(root,dir))
                

def deleteSampleVideos(dir):
    for root, directories, filenames in os.walk(dir):
        for f in filenames:
            pos = f.rfind('.')
            type = f[pos:]
            if type in VIDEO_TYPES:
                if 'sample' in f.lower():
                    print os.path.join(root,f)
                    os.remove(os.path.join(root,f))
				
def processSingleVideos(dir):
	deleteSampleVideos(dir)
	processRecursiveSingleVideos(dir)
    

def getMatchedCount(dir):
    
    matched_count = 0
    videoList = [f for f in os.listdir(dir) if f[f.rfind('.'):] in VIDEO_TYPES]
    subsList = [s for s in os.listdir(dir) if s.endswith(SUB_SRT)]
    
    video, subs = videoList[0].lower(), subsList[0].lower()
    video, subs = video[video.rfind('.'):], subs[subs.rfind('.'):]
    lenCount = len(video) if len(video) > len(subs) else len(subs)
    
    for count in range(0, lenCount):
        if video[count] == subs[count]:
            matched_count = matched_count + 1

    return matched_count
    
def renameSubsByOrder(dir):
    fileCount = getVideoFilesCount(dir)
    
    if fileCount != getSubtitleFilesCount(dir):
        print "Files count mismatch"
        return
        
    if fileCount == getMatchedCount(dir):
        print "Already ordered"
        return
        
    videoList = [f for f in os.listdir(dir) if f[f.rfind('.'):] in VIDEO_TYPES]
    subsList = [s for s in os.listdir(dir) if s.endswith(SUB_SRT)]
    
    for count in range(0, fileCount):
        video = videoList[count]
        subs = subsList[count]
        pos = video.rfind('.')
        name = video[:pos]
        os.rename(subs,name+SUB_SRT)        
    
    return
	
def clubVideosFolder(dirFolder):
    for root, directories, filenames in os.walk(dirFolder):
        for dir in directories:
            for f in os.listdir(dir):
                pos = f.rfind('.')
                type = f[pos:]
                if type in DEL_FILES:
                    os.remove(os.path.join(dir,f))
                    continue
                try:
                    os.rename(os.path.join(root,dir,f),os.path.join(root,f))        
                except WindowsError as err:
                    print err, os.path.join(root,dir,f)                
            os.rmdir(os.path.join(root,dir))
			
	
if __name__ == "__main__":

    os.chdir(SRC_DIR)
    #SRC_DIR = os.getcwd()
    #processSingleVideos(SRC_DIR)
    #clubVideosFolder(SRC_DIR)
    renameSubsByOrder(SRC_DIR)