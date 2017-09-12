#!/usr/bin/env python

# Delete the interim folders node_modules, bower_components, typings in angular projects recursively
#
# Set up: None
#
# Command line inputs: None
# In file inputs: Give the folder name as SRC_DIR
# Runtime inputs: None

import os
import sys
import shutil

SRC_DIR = "D:\\node-py\\Coursera\\angular"

def removeNpmBower(path):
    #bower_components,node_modules
    print path
    try:
        #os.remove(path)
        shutil.rmtree(path)
    except WindowsError as err:
        print err

def processDirectory(dir):
    for root, directories, filenames in os.walk(dir):
        for d in directories:
            if d == "bower_components" or d == "node_modules" or d == "typings":
                removeNpmBower(os.path.join(root, d))

if __name__ == "__main__":
    processDirectory(SRC_DIR)