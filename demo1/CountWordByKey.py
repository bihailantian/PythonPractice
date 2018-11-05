#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，
请统计出你认为每篇日记最重要的词。
'''

def count(path):
    '''
    统计单词
    @param path 文件路径
    '''

    with open(path, 'r', encoding='utf-8') as f:
        # 空列表
        word_list = []
        # 正则表达式
        #word_reg = re.compile(r'\w+')
        for line in f:
            # 替换除了n't这类连字符外的所有非单词字符和数字字符
            line = re.sub(r'(n[\']t)|([\W\d])'," ",line)
            
            #split()默认以空格分割
            line_words = line.split()
            
            #通过在列表末尾追加可迭代对象中的元素来扩展列表
            word_list.extend(line_words)

        words_dict = dict(Counter(word_list)) #使用Counter统计
        for k, v in words_dict.items():
            print(k, v)