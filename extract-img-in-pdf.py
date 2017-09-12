import os
import shutil

os.chdir('F:\\img-pdf')
curdir = os.getcwd()
#print os.getcwd()
#os.system ("echo hello")
muagent = '.\utils\mutool.exe'
dst = 'F:\\ls'
imageCounter = 0

def renamepdf(file, counter):
    name = "book"+str(counter)+".pdf"
    print name
    os.rename(f,name)
    return name
    
def extractimages(name, curdir):
    fdir = name[:-4]
    print fdir
    os.mkdir(os.getcwd()+'\\'+fdir)
    os.chdir(os.getcwd()+'\\'+fdir)
    os.system(muagent + ' extract .\\..\\' + name)
    os.chdir(curdir)

def removettf(f, curdir):
    if f.endswith(".pdf"):
        return
    os.chdir(curdir+'\\'+f)
    for f1 in os.listdir(os.getcwd()):
        if f1.find(".ttf") != -1:
            os.remove(f1)
    os.chdir(curdir)    

def copyimages(f):
    global imageCounter
    if f.endswith(".pdf"):
        return
    os.chdir(curdir+'\\'+f)
    print os.getcwd(), image
    for f1 in os.listdir(os.getcwd()):
        shutil.copy2(f1, dst+'\\image'+str(image)+'.png')
        imageCounter = imageCounter + 1
    os.chdir(curdir)
    return imageCounter
    
    
if __name__ == "__main__":

    # rename the pdf files
    booksCounter = 0
    for f in os.listdir(curdir):
        booksCounter = booksCounter + 1
        name = renamepdf(f, booksCounter)

    # extracting the images
    for f in os.listdir(curdir):
        extractimages(f, curdir)

    # remove the ttf files
    for f in os.listdir(curdir):
        removettf(f, curdir)        

    #copying the images to common folder
    os.mkdir(dst)
    for f in os.listdir(curdir):
        imageCount = copyimages(f)
        print imageCount