#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
'''

from PIL import Image,ImageDraw,ImageFont,ImageColor

def addNumber(image,count):
    #创建一个Drawd对象
    draw = ImageDraw.Draw(image)
    #字体对象
    imFont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    #颜色
    fillcolor = ImageColor.colormap.get('red')
    width, height = image.size
    draw.text((width-30, 0), str(count), font= imFont, fill=fillcolor)
    image.save("result.png", 'png')
    image.show()



if __name__ == '__main__':
    #使用相对路径
    im = Image.open("..\images\ic_user.png")
    print(im.format,im.size,im.mode)
    #显示图片
    #im.show()
    addNumber(im,3)
    