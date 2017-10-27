#!/usr/bin/env python

# Convert images with adequate resolution to landscape and portrait for wallpapers
#
# Set up:
#   pip install Pillow
#
# Command line inputs: None
# In file inputs:
#   Give the images folder as SRC_DIR
#   Give the output folder as DEST_LS for landscape, DEST_PT for portrait
# Runtime inputs: None

import os
import shutil
from PIL import Image

SRC_DIR = 'E:\\test\\dt\\'
DEST_LS = SRC_DIR + '..\\ls\\' 
DEST_PT = SRC_DIR + '..\\pt\\'
    
def isPotrait(file):
    im = Image.open(file)
    return im.size[0] < im.size[1]   
    
def rotateSave(file, dest, type):  
    im = Image.open(file)
    new_im = im.rotate(type)
    print dest
    new_im.save(dest)    
            
def splitImages(dir):
    for root,dirs,files in os.walk(dir):
        for f in files:
            file = os.path.join(root,f)
            if isPotrait(file):
                shutil.copy2(file, DEST_PT)
                rotateSave(file, os.path.join(DEST_LS,f), 270)
            else: 
                shutil.copy2(file, DEST_LS)
                rotateSave(file, os.path.join(DEST_PT,f), 90)
            os.remove(file)    
           
def isLowRes(file):    
    im = Image.open(file)
    #print im.info#, im.info['dpi']
    return im.size[0] < 1000           
           
def removeLowRes(dir):
    for f in os.listdir(dir):
        file = os.path.join(dir, f)
        if isLowRes(file):
            os.remove(file)
            
if __name__== "__main__":
    splitImages(SRC_DIR) 
    removeLowRes(DEST_LS)

    
def isLandscape(file):
    im = Image.open(file)
    return im.size[0] > im.size[1]        
    
def displayInfo(file):
    info = os.stat(file)
    im = Image.open(file)
    size = info.st_size/(1024.0*1024.0)
    print file, (int)(size*100)/100.0, "MB", im.size, im.format    
    
def rotateSave(file):  
    im = Image.open(file)
    new_im = im.rotate(90)
    new_im.save(file)
    
def flipSave(file):  
    im = Image.open(file)
    new_im = im.rotate(180)
    new_im.save(file)

def changeToLandscape(dir):    
    for file in os.listdir(dir):
        if isPotrait(file):
            rotateSave(file)