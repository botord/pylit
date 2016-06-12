#!/usr/bin/env python
# coding=utf-8

import re 
import urllib

r1 = r"\d{3,4}-?\d{8}"
url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B1%DA%D6%BD&fr=ala&ala=1&pos=0&alatpl=wallpaper&oriquery=%E5%A3%81%E7%BA%B8#z=0&pn=&ic=0&st=-1&face=0&s=0&lm=-1"
def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#example: reg = r'src="(.*?\.jpg)" width'
#"hoverURL":"http://img5.imgtn.bdimg.com/it/u=582153656,4266352363&fm=23&gp=0.jpg"

def get_Img(html):
    reg = r'\"hoverURL\":\"(.*\.jpg)\"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for i in imglist:
        urllib.urlretrieve(i,'%s.jpg'%x)
        x += 1

    return imglist


html = get_html(url)
get_Img(html)

