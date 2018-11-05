#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

import os

from collections import Counter
import re


def readFileContent(path):
    '''
    读取文本内容
    @param path 文件路径
    '''
    file = open(path,mode = 'r',encoding = 'utf-8')
    print('文件名:',file.name)
    line = file.read()
    file.close()
    return line
    
    
def count(path):
    with open(path, 'r', encoding='utf-8') as f:
        # 空列表
        word_list = []
        # 正则表达式
        #word_reg = re.compile(r'\w+')
        for line in f:
            # 替换除了n't这类连字符外的所有非单词字符和数字字符
            line=re.sub(r'(n[\']t)|([\W\d])'," ",line)
            
            #split()默认以空格分割
            line_words = line.split()
            
            #通过在列表末尾追加可迭代对象中的元素来扩展列表
            word_list.extend(line_words)

        words_dict = dict(Counter(word_list)) #使用Counter统计
        for k, v in words_dict.items():
            print(k, v)
    
if __name__ == '__main__':
    #读取文本内容
    path = "..\\file\\countWord.txt"
    content = readFileContent(path)
    print(content)
    print("\n------------------------------------------------\n")
    count(path)