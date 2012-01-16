#!/usr/bin/python

import os,sys,getopt

try:
    (opts,args) = getopt.getopt(sys.argv[1:],"",[])
except:
    print "usage: cmd <srcDir>"
    exit() 

srcDir = args[0]

indentOpts = "-bap -bbb -bbo -nbc -bl -bli0 -bls -c33 -cd33 -ncdb -ncdw -nce -cli4 -cp33 -d0 -nbfda -di2 -nfc1 -nfca -hnl -ip5 -l80 -lp -nprs -nsc -nsob -nss -i4 -ts4 -ut"

indentCmd = os.path.join("/usr/bin","indent")

print "format source file in %s" % srcDir

#for fileLoop in `find $SRC_DIR -name '*.c' -o -name '*.h' `:
#for (top,dirs,files) in os.walk(srcDir):
#    print "os.walk--> %s" % files
    #os.system("%s %s %s" % (indentCmd,fileLoop,indentOpts)) 
  #  rm -f $i~
#    print "---------------------------------------"

def pfnPrint(v_arg,v_dir,v_files):
  print "*"*60
  for fileLoop in v_files:
    print os.path.join(v_dir,fileLoop)

os.path.walk(srcDir, pfnPrint, ())


