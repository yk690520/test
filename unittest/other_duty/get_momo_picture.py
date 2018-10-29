#此模块用来获取陌陌的个人动态图片
import requests
from lxml.html import parse
from lxml import html
import time
import logging,os
import traceback
import urllib.request as request

#载入陌陌网址# 文件
def __loadFile(path):
    links=[]
    with open(path) as file:
        while True:
            link=file.readline()
            if not link:
                break
            link = str.strip(link)
            if 'http://' in link:
                links.append(link)
    return links

#读取陌陌并保存背景图
def __getBackground(location,link):
    global count
    response=requests.get(link)
    doc=html.fromstring(response.text)
    imgurls=[img.get('src') for img in doc.xpath('/html/body/div[2]/div[2]/div[3]/img')]
    for img in imgurls:
        img=img.replace("_S","_L")
        request.urlretrieve(img,"%s\\%s.jpg" % (location,count))
        print("获取中%s" % img)
        count+=1
    pass
#陌陌获取图片实际使用方法
def getMomo(location,path):

    '''
    保存图片的位置，
    :param location:
    :param path:链接读取位置
    :return:
    '''
    global count
    if not os.path.exists(location):
        os.mkdir(location)
    if not os.path.exists(path):
        return "未找到【陌陌链接】存储文件，请确认是否已经执行【步骤1】"
    count = 1
    links = __loadFile(path)
    for link in links:
        try:
            __getBackground(location, link)
        except:
            print()

def out_demo(path):

    '''
    输出一个样例文件
    :param path:
    :return:
    '''
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
    with open(path,mode="w+") as file:
        file = open(path, mode="w+")
        file.writelines("请将陌陌的个人动态链接复制到此")
        file.close()

if __name__=="__main__":
    getMomo()
