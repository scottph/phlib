#!/usr/bin/python3.1

import os,sys,re
ipstr=os.popen('ifconfig eth0').read()


print('*'*50 + "\n" + ipstr + '*'*50 )
