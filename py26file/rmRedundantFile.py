#!/usr/bin/python3.1

import os,sys,re

os.chdir('/mnt/udisk/windows/photo/2009_10')
startDir=os.getcwd()
iCount=0

def sameFile(v_src,v_dst):
    if os.path.getsize(v_src)==os.path.getsize(v_dst):
       if os.path.basename(v_src)==os.path.basename(v_dst):
           if os.path.dirname(v_src)!=os.path.dirname(v_dst):
               return True
    else:
       return False 

def rmRedundant(v_src,v_dst):
    if sameFile(v_src,v_dst):
        print("found!\n\tsrc=%s\n\tdel dst=%s\n ********\n" % (v_src,v_dst))   
        os.remove(v_dst)
        global iCount
        iCount=iCount+1
        if iCount > 20:
           print("suc to del %d files..." % iCount)
           sys.exit()

def rmFile(v_file, v_dstDir):
    for (root,dirs,files) in os.walk(v_dstDir):
      [rmRedundant(v_file, os.path.join(root,f)) for f in files]
            

for (root,dirs,files) in os.walk(startDir):
    [rmFile(os.path.join(root,f),startDir) for f in files]
#        srcFile=os.path.join(root,fileName)
#        rmFile(srcFile, startDir)  

print("%d files done..." % iCount)
