#!/usr/bin/python3.1

import os,sys,getopt

try:
    (opts,args) = getopt.getopt(sys.argv[1:],"",[])

    svr = args[0]
    user = args[1]
    pwd = args[2]
    cmdfile = args[3]
    
    expCmd = os.path.join("/sw/phlib/tclfile", "sshCmd.exp") 

    print("exp={0},svr={1},user={2},pwd={3},file={4}".format(expCmd, svr, user, pwd, cmdfile))
    os.system("{0} {1} {2} {3} {4}".format(expCmd, svr, user, pwd, cmdfile))

except:
    print("usage: cmd <svr> <user> <pwd> <cmdfile>")
    exit()

