from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import string
import re

html = urlopen("https://baike.baidu.com/item/%E5%BC%95%E8%84%9A?fromtitle=%E7%AE%A1%E8%84%9A&fromid=15513588&fromModule=lemma_search-history")
bsObj = BeautifulSoup(html, features="html.parser")

try:
    print(bsObj.find('div',attrs={"class":"para","label-module":"para","data-pid":"1"}))
except AttributeError:
    print("failed.")