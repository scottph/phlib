#!/usr/bin/python
#-*-coding: utf-8-*-

import os,re,sys,getopt

try:
    (opts,args)=getopt.getopt(sys.argv[1:],"",[])
except:
    print("usage: cmd <file>")
    exit(1)

try:
    fileName=os.path.join("/sw/phlib/py26file", args[0])
    
    tmpFile=os.path.splitext(fileName)[0]+'.tmp'
    
    print("fileName={0}, tmpFile={1}".format(fileName,tmpFile))
    
    wtHandle=open(tmpFile, 'w')

    patObj = re.compile(r"^([1-9])")
    for line in open(fileName,'r'):
        searchObj = patObj.search(line)
        if searchObj:
            subWord = '\n' + searchObj.group(1) 
            newline = patObj.sub(subWord, line)
        else:
            newline=line
        #newline = newline.lstrip()
        #newline = newline.rstrip()
        #newline = newline.strip()
        wtHandle.write(newline)  
    
    wtHandle.close()

except:
    print("fail to handle...")
    exit(1)
