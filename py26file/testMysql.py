#!/usr/bin/python 
#-*-coding: utf-8 -*-

import os,sys,re,MySQLdb

def grantUser():
    try:
        conn0 = MySQLdb.connect(host='localhost',user='root',passwd='123456')
        cur0 = conn0.cursor()
        cur0.execute('grant all on mp3db.* to "ph"@"localhost"')
        cur0.close()
        conn0.close()
    except:
        print("fail to grant auth...")
        exit(1)

def createDb():
    try:
        conn = MySQLdb.connect(host='localhost',user='ph',passwd='123456')
    
        #create database
        cur = conn.cursor()
    
        cur.execute('create database if not exists mp3db')
    
        print("after create database...")
    
        #select database
        conn.select_db('mp3db')
    
        #create table
        cur.execute('create table if not exists singer (name varchar(20),sex varchar(1))')
    
        #insert record
        values = []
        for line in open("./mp3.tmp",'r'):
            name = line.strip()
            values.append((name, 'M'))
    
        cur.executemany('insert into singer values(%s,%s)', values)
    
        cur.close()
        conn.close()
    
    except:
        print("fail")
        exit(1)

# ********************main*************************

try:
    conn = MySQLdb.connect(host='localhost',user='ph',passwd='123456')
except MySQLdb.Error,e:
    print("fail to connect...")
    exit(1)

try:
    #create database
#   grantUser()
#   createDb()

    #select database
    conn.select_db('mp3db')

    cur = conn.cursor()

    #show all
    sqlCmd = 'select * from singer'
    num = cur.execute(sqlCmd)
    rets = cur.fetchmany(num)
    for iLoop in rets:
        print iLoop

    cur.scroll(0,mode='absolute')


    #close 
    cur.close()
    conn.close()

except:
    print("fail to handle...")
    exit(1)

