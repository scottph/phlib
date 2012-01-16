#!/usr/bin/env python

import os,sys,getopt,pdb

#just print files
def pfnPrint(v_arg,v_dir,v_files):
    print "*"*60
    for fileLoop in v_files:
        if os.path.splitext(fileLoop)[1] == ".c":
            print("{0}".format(os.path.join(v_dir,fileLoop)))

#handle format c files
def pfnFormatC(v_arg,v_dir,v_files):
    print "*"*60
    print "format c files in %s" % v_dir

    Opts = "-bap -bbb -bbo -nbc -bl -bli0 -bls -c33 -cd33 -ncdb -ncdw -nce -cli4 -cp33 -d0 -nbfda -di2 -nfc1 -nfca -hnl -ip5 -l80 -lp -nprs -nsc -nsob -nss -i4 -ts4 -ut"

    cmd = os.path.join("/usr/bin","indent")

    for fileLoop in v_files:
        if os.path.splitext(fileLoop)[1] == ".c":
            os.system("%s %s %s" % (cmd, os.path.join(v_dir,fileLoop), Opts))

try:
    (opts,args) = getopt.getopt(sys.argv[1:],"",[])

    #pdb.set_trace()
    srcDir = args[0]
    action = args[1]

    if (action == "formatc") :
        pfnFunc = pfnFormatC
    elif (action == "print") :
        pfnFunc = pfnPrint
    else:
        print("wrong parameter...")
        sys.exit(1)

    os.path.walk(srcDir, pfnFunc, ())

except:
    print("fail to handle...")
    sys.exit(1)

