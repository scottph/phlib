#!/usr/bin/env python

import os,sys,socket


try:
    ret = socket.getaddrinfo(sys.argv[1], None)

    print ret[0][4]

except:
    print("fail to handle...")
    sys.exit(1)
