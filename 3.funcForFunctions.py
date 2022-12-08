'''
    该文件实现了几个功能：
    1、获取页面所有内链的列表
    2、获取页面所有外链的列表
    3、获取一个随机外链
    4、进入一个随机外链并继续搜索外链
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import time
import random

pages = set()
random.seed(time.time())

# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a",
        href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, features="html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getExternalLinks(internalLinks[random.randint(0,
                len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

'''
    只追踪搜寻到的外链
    如果某一个网站里面一个外链都没有，程序会一直跳不出这个网站
    改进版：getAllExternalLinks函数
'''
def followExternalOnly(startingSite):
    # externalLink = getRandomExternalLink("http://oreilly.com")
    externalLink = getRandomExternalLink("https://baike.baidu.com")
    print("随机外链是："+externalLink)
    followExternalOnly(externalLink)

'''
    收集网站上发现的所有外链列表,并记录每一个外链
    获取页面上所有内链，加入列表，获取页面上所有外链，加入列表
'''
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, features="html.parser")
    internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是："+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

# followExternalOnly("http://oreilly.com")
# followExternalOnly("https://baike.baidu.com")
getAllExternalLinks("https://baike.baidu.com")