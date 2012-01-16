#!/usr/bin/env python

import os,sys,getopt

try:
    (opts,args) = getopt.getopt(sys.argv[1:],"",[])
except getopt.GetoptError:
    exit()

cmdName=args[0]
savePath="/sw/phlib/manfile"

try:
    os.system('man {0} | col -b > {1}/{0}.txt'.format(cmdName,savePath))
except:
    print("bad parameter...")
    exit()
