#!/usr/bin/python

import os,sys,re,MySQLdb

def mvMp3(v_src, v_dst)
    os.system('mv v_src v_dst')

def getDst(v_mp3)
    conn = MySQLdb.conn(host='localhost',user='ph',passwd='123456',db='mp3db')
    cur = conn.cursor()
    num = cur.execute('select %s from songs where name=%s')
    if num == 1 :
        linecur.fetchone('')
        num = cur.execute('select ') 
    else:
        return 0


try:
    srcDir = '/sw/mp3'
    dstDir = '/sw/phlib/py26file/mp3'    

    

except:
    print("handle fail...")
    exit(1)
