#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小(iPhone 5: 640x1136)

分析：
    1.遍历目录，找出所有是图片的文件(可通过后缀名识别)
    2.只修改分辨率，不修改文件名
'''


import os
from PIL import Image

fextensionList = [".jpg",".png",".jpeg",".bmp"]

def findImgByPath(dirpath):
    '''
    通过路径查找图片
    @param dirpath 目录
    '''
    pathList = []
    for dirpath,dirname,filenames in os.walk(path):
        for file in filenames:
            #print("dirpath=",dirpath)
            #print("file=",file) #file 文件名+后缀
            #print("----->",os.path.splitext(file))
            
            #分离文件名与扩展名
            fextension = os.path.splitext(file)[1]
            if fextension in fextensionList:
                fullpath = os.path.join(dirpath,file)
                pathList.append(fullpath)
                print(fullpath)
    return pathList


def alterImgResolution(imgPath):
    '''
    修改图片分辨率
    @param imgPath 图片路径
    '''
    imgInfo = os.path.splitext(imgPath)
    name = imgInfo[0] + "_640_1136"
    fextension = imgInfo[1]
    im = Image.open(imgPath)
    out = im.resize((1136,640),Image.ANTIALIAS)
    out.save(name+fextension)
    
    
    
    
    
    
    
if __name__ == '__main__':
    #当前文件目录
    path = os.getcwd()
    #path = "D:\Python\PythonPractice"
    pathList = findImgByPath(path)
    print("\n-----------------------------\n")
    print(pathList)
    for file in pathList:
        alterImgResolution(file)
    
    