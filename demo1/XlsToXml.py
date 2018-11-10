#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
将student.xls 文件中的内容写到 student.xml 文件中
'''

import xlrd


def read03Excel(path):
    #读取Excel文件的内容
    wb = xlrd.open_workbook(filePath)
    sheets = wb.sheet_names()
    print("sheets=",sheets)
    worksheet = wb.sheet_by_name(sheets[0])
    data = {}
    for i in range(0,worksheet.nrows):
        key = ''
        valList = []
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")
            if j == 0:
                key = worksheet.cell_value(i, 0)
            else:
                valList.append(worksheet.cell_value(i, j))
        print()
        data[key]=valList
    print("====================")
    print(data)
    return data


if __name__ == '__main__':
    filePath = "..\\file\\student.xls"
    fileSavePath = "..\\file\\student.xml "
    data = read03Excel(filePath)
    
    #写入xml
    fo = open(fileSavePath, "w+")
    fo.writelines("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    fo.write("\n")
    fo.writelines("<root>")
    fo.write("\n")
    fo.writelines("<students>")
    fo.write("\n")
    fo.writelines("<!--\n学生信息表 \n\"id\" : [名字, 数学, 语文, 英文] \n-->")
    fo.write("\n")
    fo.writelines(str(data))
    fo.write("\n")
    fo.writelines("</students>")
    fo.write("\n")
    fo.writelines("</root>")
    fo.flush()
    fo.close()