#!/usr/bin/python
#-*- coding: utf-8 -*-
import os,re,sys,getopt

try:
    (opts,args) = getopt.getopt(sys.argv[1:], "", [])
except:
    print("usage: cmd <file>")
    exit(1)

fileName = args[0]

tmpFile = os.path.splitext(fileName)[0] + '.tmp'

print("format file = {0}".format(fileName))

wtHandle=open(tmpFile,'w')

inPat = '[ ]+(.*)ta的热歌'
inObj = re.compile(inPat)

exPat = ('\*', '趋势', '\s[\d]+\s')

for line in open(fileName,'r'):
    if re.search(exPat[0], line):
        continue
    elif re.search(exPat[1], line):
        continue
    elif re.search(exPat[2],line):
        continue
    else:
        searchObj = inObj.search(line)
        if searchObj:
            newtmp=searchObj.group(1)
        else:
            newtmp = line
        newline = newtmp.strip()

        if newline:
            newline = newline + '\n'
            wtHandle.write(newline)
     

wtHandle.close()


