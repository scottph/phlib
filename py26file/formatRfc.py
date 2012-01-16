#!/usr/bin/env python

import os,re,sys,getopt,pdb

def wtLine(v_line, v_wtHandle):
    if patObj1.search(v_line):
        wtHandle.write(v_line)

try:
    (opts, args) = getopt.getopt(sys.argv[1:], '','')
except:
    print("fail to get opt...")
    sys.exit(1)

try:
    fileName = args[0]

    pattern = 'THIS CANNOT BE POSSIBLE...'
    if len(args) == 2:
        pattern = args[1]
        
    pdb.set_trace()
    
    bakFile=os.path.splitext(fileName)[0]+".bak"
    cmd = 'cp ' + fileName + ' ' + bakFile
    os.system(cmd)
    
    print("you input: file={0}, handle pattern={1}".format(fileName,pattern))
    
    wtHandle=open(fileName, 'w')
    
    patObj=re.compile(pattern)

    for line in open(bakFile, 'r'):
        #[wtHandle.write(line) for line in open(tmpFile,'r') if not patObj.search(line)]
        #[print(line) for line in open(tmpFile,'r') if len(line) < 5]
        tmpline = line.strip()
        if tmpline:
            if not patObj.search(tmpline):
                wtHandle.write(line)

    wtHandle.close()

except:
    print("handle fail, usage: cmd <rfcfile> <pattern>...")
    sys.exit(1)
