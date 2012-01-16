#!/usr/bin/python3.1
import os,re,sys,getopt


fileName = os.path.join(os.getcwd(),sys.argv[1])
pattern = sys.argv[2]
subWord = sys.argv[3]

tmpFile = os.path.splitext(fileName)[0] + '.tmp'

print("pattern={0},subWord={1}".format(pattern,subWord))

wtHandle=open(tmpFile,'w')

patObj = re.compile(pattern)
for line in open(fileName,'r'):
    newline = patObj.sub(subWord,line)
    wtHandle.write(newline)

wtHandle.close()


