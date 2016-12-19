def isolateVideos(dir): # not required anymore
    for f in os.listdir(dir):
        if os.path.isfile(f):
            pos = f.rfind('.')
            type = f[pos:]
            if type in videoTypes:
                name = f[:pos]
                newDir = os.path.join(dir,name)
                os.makedirs(newDir)
                os.rename(os.path.join(dir,f),os.path.join(newDir,f))
        

def renameSubsByName(dir): # unused function
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