#!/usr/bin/env python

# Delete the interim folders node_modules, bower_components, typings in angular projects recursively
#
# Set up: None
#
# Command line inputs: None
# In file inputs: Give the folder name as SRC_DIR
# Runtime inputs: None

import os
import getopt, sys
import shutil

SRC_DIR = "D:\\node-py\\Coursera\\angular"

def removeInterim(path):
    # bower_components, node_modules, typings
    print path
    #try:
    #    shutil.rmtree(path) #os.remove(path)
    #except WindowsError as err:
    #    print err

def processDirectory(dir):
    print "Processing", dir
    for root, directories, filenames in os.walk(dir):
        for d in directories:
            if d == "bower_components" or d == "node_modules" or d == "typings":
                removeInterim(os.path.join(root, d))

def usage():
    print "Usage: $0 -d'dir' or $0 --dir='dir'"

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:", ["help", "dir="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    if (len(opts) == 0 and len(args) == 0):
        processDirectory(SRC_DIR)
    elif (len(opts) == 0 and len(args) == 1):
        processDirectory(args[0])

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--dir"):
            processDirectory(a)
        else:
            assert False, "unhandled option"