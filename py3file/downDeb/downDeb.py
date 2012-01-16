#!/usr/bin/python3.1

#usage:
#write debs to be downloaded into a txt file, one deb per line.
#then：
#python getmp3.py cfg.txt

#-*- coding: utf-8 -*-
import sys
import os
import re
#import urllib2

if 'debNames.txt' != sys.argv[1] :
    print("usage: python3.1 downDeb.py debNames.txt")
    sys.exit()

if os.path.isfile(sys.argv[1]):
    cfgFileName = sys.argv[1]
else:
    print("usage: python3.1 downDeb.py debNames.txt")
    sys.exit()
       
try:
    cfgFile = open(cfgFileName,'r')
   
except IOError:
    print('fail to open debNames.txt!')
    sys.exit()

for eachLine in cfgFile:
    debName = eachLine.strip()
    if not debName:
        continue
    
    print("/*****************************************************/")
    print('\n now try install: %s...\n' % debName)
    print("/******************************************************/")
    cmd = 'apt-get install %s' % debName
    os.system(cmd)
           
print("/*******************************************************/")
print('done...')
