import os
import sys
import shutil


curDir = ""
videoTypes = ['.mp4','.avi','.mkv','.vob','.flv']
subsType = ['.srt','.sub']
SUB_SRT = ".srt"
DEL_FILES = ['.txt','.zip','.nfo','.db','.jpg','.png','.rar']

                
def getNumofVideoFiles(dir):
    count = 0
    for f in os.listdir(dir):
        pos = f.rfind('.')
        type = f[pos:]
        
        if type in videoTypes:
            count = count + 1
            
    return count
                
def renameSubsByOrder(dir):
    fileCount = getNumofVideoFiles(dir)
    #if fileCount != getNumofSubFiles(dir):
    #    print "Files count mismatch"
    #    return
        
    videoList = [f for f in os.listdir(dir) if f[f.rfind('.'):] in videoTypes]
    subsList = [s for s in os.listdir(dir) if s.endswith(SUB_SRT)]
    
    for count in range(0, fileCount):
        video = videoList[count]
        subs = subsList[count]
        pos = video.rfind('.')
        name = video[:pos]
        print subs + "  =>  " + name+SUB_SRT
        os.rename(subs,name+SUB_SRT)        
    
    return

def processFolder(dirFolder):
    for root, directories, filenames in os.walk(dirFolder):
        for dir in directories:
            for f in os.listdir(dir):
                pos = f.rfind('.')
                type = f[pos:]
                if type in DEL_FILES:
                    os.remove(os.path.join(dir,f))
                    continue
                #print os.path.join(root,dir,f)
                try:
                    os.rename(os.path.join(root,dir,f),os.path.join(root,f))        
                except WindowsError as err:
                    print err, os.path.join(root,dir,f)                
            os.rmdir(os.path.join(root,dir))    

			
if __name__ == "__main__":
    os.chdir('F:\seasons\Seinfeld\Season 8')
    curDir = os.getcwd()
    renameSubsByOrder(curDir)
    #processFolder(curDir)
