#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
一个HTML文件，找出里面的正文
'''

import os

path = "..\\file\\ImageFont Module — Pillow (PIL Fork) 5.4.0.dev0 documentation.html"
isHTMLBody = False


startStr = "<body"
endStr = "</body>"

with open(path,'r',encoding='utf-8') as f:
    for line in f:
        if line.startswith(endStr,0,len(endStr)):
            isHTMLBody = False
            break
        if isHTMLBody:
            print(line)
        
        if line.startswith(startStr,0,len(startStr)):
            isHTMLBody = True
        
       