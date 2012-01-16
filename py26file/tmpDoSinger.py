#!/usr/bin/python

import os,sys

files = ('songs',)

for iLoop in files:
    if os.path.exists(iLoop+".txt"):
        os.remove(iLoop + ".txt")

    os.rename(iLoop + ".tmp", iLoop + ".txt")
