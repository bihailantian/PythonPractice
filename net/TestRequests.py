#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import urllib.request
import json

# 使用urllib 方式获取

path = "http://gank.io/api/today";

response = urllib.request.urlopen(path);
#输出的是十六进制的
#print(response.read())

# decode('unicode-escape'):解决输出中文显示 '\u871c\u7c89/\u6563\u7c89' 的问题
print(response.read().decode('unicode-escape'))
