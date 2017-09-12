import os
import time
import shutil
from datetime import datetime

SRC_FILE = "C:\Users\lraju\Dropbox\others-hr\important.txt"
DST_FILE = "D:\Others-HR\hr-docs\important.txt"

def displayInfo(file):
    info = os.stat(file)
    modified_time = info.st_mtime
    #size = info.st_size/(1024.0)
    #print file, (int)(size*100)/100.0, "KB"
    print "Last modified:", datetime.fromtimestamp(modified_time)
    
def isRecentlyModified(file):  # <24 hrs
    modified = datetime.fromtimestamp(os.stat(file).st_mtime)
    current = datetime.now()#time.time()
    diff = current - modified
    return diff.days==0
    
def updateLocalFile(src, dst):    
    if isRecentlyModified(src):
        shutil.copy(src, dst)
        print "Recently modified"

if __name__=="__main__":    
    updateLocalFile(SRC_FILE, DST_FILE)
    