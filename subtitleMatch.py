import os
import sys
import shutil

curDir = ""
videoTypes = ['.mp4','.avi','.mkv','.vob','.flv']
subsType = ['.srt']
SUB_SRT = ".srt"
DEL_FILES = ['.txt','.zip','.nfo','.db','.jpg','.png','.rar']
THRESHHOLD = 7
#checkPoint = 17

def getNumofVideoFiles(dir):
    count = 0
    for f in os.listdir(dir):
        pos = f.rfind('.')
        type = f[pos:]
        
        if type in videoTypes:
            count = count + 1
            
    return count
    
def getNumofSubFiles(dir):
    count = 0
    for s in os.listdir(dir):
        if s.endswith(SUB_SRT):
            count = count + 1
    return count
    
def renameSingleVideoSubs(dir):
    name = ""
    
    for f in os.listdir(dir):        
        pos = f.rfind('.')
        type = f[pos:]
        if type in DEL_FILES:
            os.remove(os.path.join(dir,f))
            #os.rename(os.path.join(dir,f),os.path.join('D:\Ent',f))
        elif type in videoTypes:
            name = f[:pos]
    
    for s in os.listdir(dir):                
        if s.endswith(SUB_SRT):
            subName = name+SUB_SRT
            if s != subName:
                if os.path.exists(os.path.join(dir,subName)):
                    os.remove(os.path.join(dir,s))
                try:
                    os.rename(os.path.join(dir,s), os.path.join(dir,subName))        
                except WindowsError as err:
                    print err, os.path.join(dir,s)
    return
    
def getBreakPoint(dir):
    
    breakPoint = 0
    videoList = [f for f in os.listdir(dir) if f[f.rfind('.'):] in videoTypes]
    subsList = [s for s in os.listdir(dir) if s.endswith(SUB_SRT)]
    
    video, subs = videoList[0].lower(), subsList[0].lower()
    video, subs = video[video.rfind('.'):], subs[subs.rfind('.'):]
    lenCount = len(video) if len(video) > len(subs) else len(subs)
    
    for count in range(0, lenCount):
        if video[count] == subs[count]:
            breakPoint = breakPoint + 1

    return breakPoint
    
def renameSubsByOrder(dir):
    fileCount = getNumofVideoFiles(dir)
    if fileCount != getNumofSubFiles(dir):
        print "Files count mismatch"
        return
        
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
    
def renameSubsByName(dir):
    for f in os.listdir(dir):
        pos = f.rfind('.')
        type = f[pos:]
        
        if type in videoTypes:
            name = f[:pos]                        
            match_sub = ""
            
            for s in os.listdir(dir):                
                if s.endswith(SUB_SRT):
                    pos1 = s.rfind('.')
                    name1 = s[:pos1]
                    
                    if name[:breakPoint].lower() == name1[:breakPoint].lower():
                        match_sub = s

            print match_sub + "  =>  " + name+SUB_SRT
            os.rename(match_sub,name+SUB_SRT)
    return
    
def isolateVideos(dir):
    for f in os.listdir(dir):
        if os.path.isfile(f):
            pos = f.rfind('.')
            type = f[pos:]
            if type in videoTypes:
                name = f[:pos]
                newDir = os.path.join(dir,name)
                os.makedirs(newDir)
                os.rename(os.path.join(dir,f),os.path.join(newDir,f))
                
def processFolder(dir):
    
    for s in os.listdir(dir):
        print s
        if os.path.isdir(s):
            if getNumofVideoFiles(s) == 1:
                renameSingleVideoSubs(os.path.join(dir,s))
                #return
            
    #breakPoint = getBreakPoint(dir)
    #if breakPoint < THRESHHOLD:
    #    renameSubsByOrder(dir)
    #else:
    #    renameSubsByName(dir)
        
    return
    
def processRecursiveFolder(dirFolder):
    for root, directories, filenames in os.walk(dirFolder):
        for dir in directories:
            if getNumofVideoFiles(os.path.join(root,dir)) == 1:
                print os.path.join(root,dir)
                renameSingleVideoSubs(os.path.join(root,dir))
                

def processSampleVideos(dir):
    for root, directories, filenames in os.walk(dir):
        for f in filenames:
            pos = f.rfind('.')
            type = f[pos:]
            if type in videoTypes:
                if 'sample' in f or 'Sample' in f or 'SAMPLE' in f:
                    print os.path.join(root,f)
                    os.remove(os.path.join(root,f))
                    #renameSingleVideoSubs(os.path.join(root,dir))
    
def calculateNSC():
    amt = 100
    interest = 8.5/100
    yrs = 5
    for i in range(5):
        val = amt * interest
        amt = amt + val
    print amt
    return

if __name__ == "__main__":

    os.chdir('F:\latest')
    curDir = os.getcwd()
    #processFolder(curDir)
    #isolateVideos(curDir)
    processRecursiveFolder(curDir)
    #processSampleVideos(curDir)
    #calculateNSC()

    
        
    