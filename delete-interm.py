import os
import sys
import shutil

curDir = ""

def removeNpmBower(path):
    #bower_components,node_modules
    print path
    try:
        os.remove(path)
    except WindowsError as err:
        print err

def processDirectory(dir):
    for root, directories, filenames in os.walk(dir):
        for d in directories:
            if d == "bower_components":# or d == "node_modules":
                removeNpmBower(os.path.join(root, d))

if __name__ == "__main__":
    curDir = "D:\\node-py\\Coursera\\angular"
    processDirectory(curDir)