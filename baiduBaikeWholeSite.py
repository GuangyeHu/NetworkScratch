# 采集整个百度百科网站，从顶层页面开始采集（百度百科主页）
# 然后搜索页面上的所有链接，形成列表
# 然后去采集这些链接的每一个页面
# 用Python的set集合进行链接去重，避免一个页面被采集两次
# 解决vscode code runner输出中文乱码的问题
# 设置->搜索@ext:formulahendry.code-runner ->edit in settings.json
# 进入编辑，把"python":"python-u",改成"python": "set PYTHONIOENCODING=utf8 && python -u",
# 保存即可

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import string
import re

pages = set()
def getLinks(pageUrl):
    global pages
    pageUrl = quote(pageUrl, safe=string.printable)
    try:
        html = urlopen("https://baike.baidu.com"+pageUrl, timeout=10)
    except Exception as e:
        print('a',str(e))
    bsObj = BeautifulSoup(html,features="html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/item/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
            # 我们遇到了新页面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")