from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import string
import re

pages = set()
def getLinks(pageUrl):
    global pages
    pageUrl = quote(pageUrl, safe=string.printable)
    # html = urlopen("http://en.wikipedia.org"+pageUrl)
    html = urlopen("https://baike.baidu.com"+pageUrl)
    bsObj = BeautifulSoup(html,features="html.parser")
    try:
        print("------------------\n1:")
        print(bsObj.h1.get_text())
        print("------------------\n2:")
        # print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(class_="main-content J-content").find({'data_pid':1}))
        print("------------------\n3:")
        # print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
        print(bsObj.find(class_="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link").find("a").attrs['href'])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")
        # for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        for link in bsObj.findAll("a", href=re.compile("^(/item/)")):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    # 我们遇到了新页面
                    newPage = link.attrs['href']
                    print("----------------\n"+newPage)
                    pages.add(newPage)
                    getLinks(newPage)
getLinks("")