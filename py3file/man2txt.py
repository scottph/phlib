#!/usr/bin/python3.1

import os,sys,getopt

try:
    (optlist,arglist) = getopt.getopt(sys.argv[1:],"",[])
except getopt.GetoptError:
    exit()

cmdName=arglist[0]
savePath="/sw/phlib/manfile"

try:
    os.system('man {0} | col -b > {1}/{0}.txt'.format(cmdName,savePath))
except:
    print("bad parameter...")
    exit()
