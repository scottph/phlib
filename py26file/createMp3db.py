#!/usr/bin/python

import os,sys,re,MySQLdb,pdb
#-*-conding: utf-8 -*-

def createDb(v_db):
    conn = MySQLdb.connect(host='localhost',user='root',passwd='123456')
    cur = conn.cursor()
    #cur.execute("create user 'ph'@'localhost' identified by '123456'")
    
    #why can't use %s....
    cur.execute("grant all on mp3db.* to 'ph'@'localhost'")
    cur.close()
    conn.close()
  
    conn = MySQLdb.connect(host='localhost',user='ph',passwd='123456')
    cur = conn.cursor()
    cur.execute('create database if not exists mp3db') 
    cur.close()
    conn.close() 
    print("ok create db")
        
def createTables(v_cursor):
    cur = v_cursor


    cur.execute('''create table if not exists maleSinger
                (name varchar(20) not null, 
                primary key (name),
                sex varchar(1) not null )''')
    print("ok malesinger table...")    

    cur.execute('''create table if not exists femaleSinger
                (name varchar(20) not null,
                primary key (name), 
                sex varchar(1) not null )''')
    print("ok female.")

    cur.execute('''create table if not exists teamSinger
                (name varchar(20) not null, 
                primary key (name),
                sex varchar(1) not null )''')                
    print("ok team")

    cur.execute('''create table if not exists songs
                (name varchar(40) not null, 
                singer varchar(20),
                type varchar(10),
                stars varchar(1),
                releaseDate varchar(10) )''')
    print("ok songs")


def importData(v_cur, v_table):
    #pdb.set_trace()
    fileName = '/sw/phlib/py26file/maleSinger.txt'
    values = []
    p1 = re.compile(r"^[A-Z]$")
    for line in open(fileName, 'r'):
        if p1.search(line):
           continue
        dataList = line.split()
        for iLoop in dataList:
            value = (iLoop, 'M')
            values.append(value)

    print("original len={0}".format(len(values)))
    num = v_cur.executemany("insert ignore into maleSinger values(%s, %s)", values)
    print("ok import {0}".format(num))

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #createDb('mp3db')
    conn = MySQLdb.connect(host='localhost',user='ph',passwd='123456', db='mp3db')
    cur = conn.cursor()

    #pdb.set_trace()
    #cur.execute("drop table maleSinger")
    createTables(cur)
    importData(cur, "maleSinger")

    cur.close()
    conn.close() 

except:
    print("fail to handle...")
    exit(1)

