#!/usr/bin/env python

import os,sys,socket,pdb

try:
    pdb.set_trace()
    ret = socket.gethostbyaddr(sys.argv[1]);
    print "Primary hostname:"
    print "  " + ret[0]
    print "\nAddress:"
    for item in ret[2]:
       print "  " + item


except:
    print("fail to handle...")
    sys.exit(1)
