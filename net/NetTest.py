# !/usr/bin/env python3
# -*- encoding:utf-8 -*-

import urllib.request
import http.client
import json


path = "https://gank.io/api/xiandu/categories"

host = "gank.io"
param = "api/xiandu/categories"
port = 80

def netOfHttp():
    '''
    Http网络请求
    '''
    print("netOfHttp")
    conn = http.client.HTTPSConnection(host)
    # HTTPConnection.request(method, url, body=None, headers={}, *, encode_chunked=False) 
    conn.request("GET","/api/xiandu/categories")
    response = conn.getresponse()
    print("response.status:",response.status)
    response_data = response.read()
    # json.loads():解决输出中文显示 '\u871c\u7c89/\u6563\u7c89' 的问题
    response_str = json.loads(response_data)
    print('-------------------------------------')
    print(response_data.decode("unicode-escape"))


def netOfUrllib():
    '''
    使用urllib 方式获取
    '''
    response = urllib.request.urlopen(path);
    #输出的是十六进制的
    #print(response.read())

    # decode('unicode-escape'):解决输出中文显示 '\u871c\u7c89/\u6563\u7c89' 的问题
    print(response.read().decode('unicode-escape'))



if __name__ == "__main__":
    print("主函数")
    #netOfUrllib()
    netOfHttp()