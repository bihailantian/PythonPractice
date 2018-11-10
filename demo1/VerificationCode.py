#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
 使用 Python 生成类似于字母验证码图片
'''

import random
from PIL import Image,ImageDraw,ImageColor,ImageFont

letterArr = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7', '8', '9' ]
#字符个数
codeCount = 4

# 随机颜色:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

if __name__ == '__main__':
    #print(range(len(letterArr)))
    width = 60 * 4
    height = 60
    im = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    #字体对象
    imFont = ImageFont.truetype("arial.ttf", size=40)
    #字体间隔
    intervalFont = (width)/(codeCount+1)
    #print("intervalFont=",intervalFont)
    for i in range(4):
        randint = random.randint(0,len(letterArr)-1)
        str = letterArr[randint]
        draw.text((intervalFont* (i + 1),5),str,font=imFont,fill=rndColor())
    
    im.show()