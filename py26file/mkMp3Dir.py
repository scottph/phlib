#!/usr/bin/python

import os,sys,re,getopt

try:
    (opts,args) = getopt.getopt(sys.argv[1:],'',[])
except:
    print("usage: cmd <file>")
    exit(1)

try:
    topDir = '/sw/phlib/py26file/testMp3'
    fileName = os.path.join('/sw/phlib/py26file', args[0])
    print("file={0}".format(fileName))
    if not os.path.isdir(topDir):
        os.mkdir(topDir)
    os.chdir(topDir)

    pat = re.compile(r"[A-Z]")
    print("now dir = {0}".format(os.getcwd()))
    for line in open(fileName,'r'):
        line = line.lstrip()
        line = line.rstrip()
        print("line={0}".format(line))
        if pat.search(line):
            print("got dir")
            os.chdir(topDir)
            if not os.path.isdir(line):
                os.mkdir(line)
            os.chdir(line)
        else:
            if os.getcwd() == topDir:
                continue
            print("got dirlist")
            dirList = line.split()
            for dirLoop in dirList:
                if not os.path.isdir(dirLoop):
                    os.mkdir(dirLoop)

    
except:
    print("handle fail...")
    exit(1)
