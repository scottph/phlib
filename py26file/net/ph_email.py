#!/usr/bin/env python

import os, sys, re, pdb
import email, smtplib, poplib, base64
from email.Message import Message

def connectSmtp(v_svr, v_port, v_user, v_pwd):
    svr = smtplib.SMTP(v_svr, v_port)
    svr.ehlo()
    svr.login(v_user, v_pwd)
    return svr

def sendMsg(v_svr):
    #pdb.set_trace()
    msg = '''hello,
      this is a test email...
      '''

    msg = Message()
    msg['From'] = '1512889650@qq.com'
    msg['To'] = '32281799@qq.com'
    msg['Subject'] = 'Test Msg'
    msg.set_payload(content)

    toUser = '32281799@qq.com'
    fromUser = '1512889650@qq.com'

    v_svr.sendmail(fromUser, toUser, str(msg))
    #print msg.as_string()

    return


def connectPop3 (v_svr, v_user, v_pwd):
    p3 = poplib.POP3(v_svr)
    p3.user(v_user)
    p3.pass_(v_pwd)
    return p3

def rcvMsg (v_p3):
    mailNum, size = v_p3.stat()
    hdr, origMsg, octet = v_p3.retr(1)
    msg = email.message_from_string(string.join(origMsg, '\n'))
    sub1 = msg['subject']
    print "orig sub1 = %s" % sub1
    sub2 = msg.Header.decode_header(sub1)
    print "after decode, sub2=%s" % sub2

try:
    pdb.set_trace()
    content = "this is a test content..."

    smtpSvr = 'smtp.qq.com'
    smtpUser = '1512889650@qq.com'
    smtpPwd = '******'
    smtpPort = '25'

    popSvr = 'pop.qq.com'
    popUser = '32281799@qq.com'
    popPwd = ''
    #popPort = ''

    try:
        #svr = connectSmtp(smtpSvr, smtpPort, smtpUser, smtpPwd)
        #sendMsg(svr)
        p3 = connectPop3(popSvr, popUser, popPwd)
        rcvMsg(p3)
    except:
        print("fail to sendmail...")
        sys.exit(1)
    else:
        print("send success...")

except:
    print("fail to handle...")
    sys.exit(1)
