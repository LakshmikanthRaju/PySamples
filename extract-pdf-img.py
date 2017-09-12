#!/usr/bin/env python

# Extract the images from the pdf files in original format
#
# Set up:
#   copy mutool.exe - third party tool which processes the PDF files
#
# Command line inputs: None
# In file inputs:
#   Give the source folder name as SRC_DIR
#   Give the destination folder name as DEST_DIR
#   Give the path to mutool.exe
# Runtime inputs: None

import os
import shutil


SRC_DIR = 'F:\\img-pdf'
MU_AGENT = '.\utils\mutool.exe'
DEST_DIR = 'F:\\ls'

IMG_COUNTER = 0

def renamepdf(file, counter):
    name = "book"+str(counter)+".pdf"
    print name
    os.rename(f,name)
    return name
    
def extractimages(name, src_folder):
    fdir = name[:-4]
    print fdir
    os.mkdir(os.getcwd()+'\\'+fdir)
    os.chdir(os.getcwd()+'\\'+fdir)
    os.system(MU_AGENT + ' extract .\\..\\' + name)
    os.chdir(src_folder)

def removettf(f, src_folder):
    if f.endswith(".pdf"):
        return
    os.chdir(SRC_DIR+'\\'+f)
    for f1 in os.listdir(os.getcwd()):
        if f1.find(".ttf") != -1:
            os.remove(f1)
    os.chdir(src_folder)

def copyimages(f, src_folder):
    global IMG_COUNTER
    if f.endswith(".pdf"):
        return
    os.chdir(src_folder+'\\'+f)
    print os.getcwd(), IMG_COUNTER
    for f1 in os.listdir(os.getcwd()):
        shutil.copy2(f1, DEST_DIR+'\\image'+str(IMG_COUNTER)+'.png')
        IMG_COUNTER = IMG_COUNTER + 1
    os.chdir(src_folder)
    return IMG_COUNTER
    
    
if __name__ == "__main__":
    os.chdir(SRC_DIR)

    # rename the pdf files
    booksCounter = 0
    for f in os.listdir(SRC_DIR):
        booksCounter = booksCounter + 1
        name = renamepdf(f, booksCounter)

    # extracting the images
    for f in os.listdir(SRC_DIR):
        extractimages(f, SRC_DIR)

    # remove the ttf files
    for f in os.listdir(SRC_DIR):
        removettf(f, SRC_DIR)

    #copying the images to common folder
    os.mkdir(DEST_DIR)
    for f in os.listdir(SRC_DIR):
        imageCount = copyimages(f, SRC_DIR)
        print imageCount