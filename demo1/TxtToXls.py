#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
纯文本文件 student.txt为学生信息, 里面的内容写到 student.xls 文件中。
'''

import json
import xlwt


def write03Excel(savepath,jsonStr,sheetname):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet(sheetname)
    row = 0
    
    #遍历key
    for key in jsonStr.keys():
        column = 0
        sheet.write(row,column,key)
        #print(key,jsonStr[key])
        list =  jsonStr[key]
        for value in list:
            column = column + 1
            sheet.write(row,column,value)
        row = row + 1
    
    wb.save(savepath)
    print("保存成功")

def readFileContent(path):
    '''
    读取文本内容
    @param path 文件路径
    '''
    file = open(path,mode = 'r',encoding = 'utf-8')
    #print('文件名:',file.name)
    line = file.read()
    file.close()
    return line

    
if __name__ == '__main__':
    path = "..\\file\\student.txt"
    file_student = "..\\file\\student.xls"
    content = readFileContent(path)
    jsonStr = json.loads(content)
    write03Excel(file_student,jsonStr,"student.xls")
    