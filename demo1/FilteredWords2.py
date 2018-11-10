#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，
否则打印出 Human Rights。
'''

path = "..\\file\\filtered_words.txt"


def readFileContent(path):
    word_list = []
    with open(path,'r',encoding='utf-8') as f:
        for line in f:
            word_list.append(line.strip()) #strip():方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    
    return word_list


if __name__ == '__main__':
    word_list = readFileContent(path)
    #print(word_list)
    while True:
        inputStr = input("exit：退出,请输入:")
        if inputStr == "exit":
            exit()
        for fw in word_list:
            if fw in inputStr:
                inputStr = inputStr.replace(fw,"*"*len(fw))
        print(inputStr)
