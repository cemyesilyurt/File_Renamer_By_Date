"""
File filerenamerscript.
Defines File Renamer program's runOperation method as a script.
"""
# Cem Yesilyurt
# 4/3/18
# Python 3.6.2

from os import listdir, getcwd
from os.path import exists, isfile, join, getmtime, splitext
import datetime

def runOperation(mypath, myprefix):
    
    FORBIDDEN_CHARS= ['/', '\\', ':', '*', '?', '\"', '<', '>', '|']
    
    # 1. verify mypath exists   
    if exists(mypath): pass  # directory exists
    else: return -1    # directory does not exist
         
    # 2. verify myprefix does not contain forbidden character(s)    
    for char in FORBIDDEN_CHARS:
        if char in myprefix: return -2  # myprefix contains forbidden character
        
    # 3. get list of files and their dates modified
    #    (do not look into sub-directories)
    oldFileDatesAndPaths = []
    dirList = listdir(mypath)    
    for f in dirList:
        thispath = join(mypath, f)
        if isfile(thispath):
            oldFileDatesAndPaths.append([getmtime(thispath),thispath])
    
    if len(oldFileDatesAndPaths) > 0: pass  # at least one file in directory
    else: return -3   # no files in this directory
    
    # 4. sort oldFileDatesAndPaths by date modified
    oldFileDatesAndPaths.sort()
    
    '''
    for ofdp in oldFileDatesAndPaths:
        print(str(ofdp[0]) + ", " + str(ofdp[1]))
    '''
               
    newFilePaths = []
    # for each file:
    for i in range(0, len(oldFileDatesAndPaths)):
        
        # 5. get old file path, root, extension, and file name
        fileTimeStamp = oldFileDatesAndPaths[i][0]
        oldFilePath = oldFileDatesAndPaths[i][1]
        oldRoot, ext = splitext(oldFilePath)            
       
        # 5. turn time stamp into datetime
        fileDateTime = datetime.datetime.fromtimestamp(fileTimeStamp)
        
        # 6. format datetime into desired file name
        # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        fileDateString = datetime.datetime.strftime(fileDateTime, '%Y_%m_%d')
        
        # build newFilePath
        uniquekey = str(i)
        newFileName = myprefix + '_' + uniquekey + '_' + fileDateString + ext
        newFilePaths.append(join(mypath,newFileName))
        
        
    # 7. Open each file,
    #    make new file path, 
    #    write new copy of file with new name.
    
    for i in range(0,len(newFilePaths)):
        oldpath = oldFileDatesAndPaths[i][1]
        newpath = newFilePaths[i]
        try:
            oldfile = open(oldpath, 'rb')        
            data = oldfile.read()
            newfile = open(newpath, 'wb')
            newfile.write(data)
            oldfile.close()
            newfile.close()
        except:
            return('File ' + oldpath + ' could not be copied')            
        
    # if all files successful, return number of files successfully copied and renamed
    return len(newFilePaths)