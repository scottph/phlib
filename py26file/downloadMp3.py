用法:
先将要下载的歌曲写在一个文本文件中，如song.txt,每首歌占一行.

然后运行：
python getmp3.py song.txt

下载目录为当前目录下的"Music_"

代码: [ 下载 ] [ 隐藏 ] [ 选择 ] [ 收缩 ]
代码: [ 下载 ] [ 显示 ]
使用 python 语法高亮
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import os
import re
import urllib2

cwd = os.getcwd()
lc = sys.getfilesystemencoding()
downdir = cwd+os.sep+'Music_'
print '\n下载目录为：',downdir,'\n'

if not os.path.isdir(downdir):
    print '下载目录不存在，正在创建目录：',downdir
    os.mkdir(downdir)

if os.path.isfile(sys.argv[1]):
    list_file = sys.argv[1]
else:
    list_file = cwd + os.sep + sys.argv[1]
   
try:
    f = file(list_file,'r')
   
except IOError:
    print '歌典列表打开失败，请检查文件是否存在!'
    sys.exit()

for eachLine in f:
    song = eachLine.strip()
    if not song:
        continue
   
    mp3file = downdir + os.sep + song + '.mp3'
    if os.path.isfile(mp3file):
        print '%s.mp3已经存在，转到下一首\n' % song
        continue
    url="http://box.zhangmen.baidu.com/x?op=12&count=1&title=%s$$" % urllib2.quote(song.decode(lc).encode('gbk'))

    xmlf = urllib2.urlopen(url)
    txt = xmlf.read()

    rex1 = u'(<encode>)(http://.+?/.+?\..+?)(</encode>)'
    rex2 = u'(<decode>)(.+?\..+?)(</decode>)'
    l1 = re.findall(rex1,txt)
    l2 = re.findall(rex2,txt)

    url_list = []
   
    for i in range(len(l1)):
        temp_list = re.split('/',l1[i][1])
        temp_list.pop()
        temp_list.append(l2[i][1])
        down_url = '/'.join(temp_list)
        url_list.append(down_url)

    for i in range(len(url_list)):

        extname = url_list[i].split('.')[-1]              #跳过非MP3的类型
        if extname.upper() == 'MP3':

            print '\n正在下载歌曲：%s...\n' % song
           
            cmd = 'wget %s -c -t 3 -O "%s"' % (url_list[i],downdir+os.sep+song+'.mp3')
            os.system(cmd)
           
            #multGet.MyHttpGet(url_list[i],connections = 10)
            if os.path.getsize(mp3file) < 500000L:  #小于500K的文件将被删除，并重新下载
                print '\n文件过小，可能是目标网站有限制，将尝试下一个链接\n'
                os.remove(mp3file)
            else:
                print '《%s》下载完毕！' % song
                break
print '全部下载完毕！'
