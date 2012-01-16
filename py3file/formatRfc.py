#!/usr/bin/python3.1

import os,re,sys,getopt

def wtLine(v_line, v_wtHandle):
    if patObj1.search(v_line):
        wtHandle.write(v_line)


#os.chdir("/sw/phlib/pyfile/ipv6_rfc")
#curPath=os.getcwd()
fileName=os.path.join(os.getcwd(), sys.argv[1])
pattern=sys.argv[2]

tmpFile=os.path.splitext(fileName)[0]+".cmp"

print("you input: file={0},pattern={1}".format(fileName,pattern))

cmd="cat -s {0} > {1}".format(fileName,tmpFile)
os.system(cmd) 
os.remove(fileName)


wtHandle=open(fileName,'w')

patObj=re.compile(pattern)
[wtHandle.write(line) for line in open(tmpFile,'r') if not patObj.search(line)]
#[print(line) for line in open(tmpFile,'r') if len(line) < 5]
wtHandle.close()

