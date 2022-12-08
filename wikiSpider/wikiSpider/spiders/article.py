'''
    修改python网络数据采集书中代码，添加start_requests函数，
    修改parse函数：
        title = response.css('h1::text').extract_first()修改为
        title = response.css('h1 span::text').extract_first()
'''
import scrapy
from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article

# 该类仅用于维基词条页面的采集
class ArticleSpider(Spider):
    name="article"
    
    def start_requests(self):
        urls = [
            "http://en.wikipedia.org/wiki/Python_%28programming_language%29",
            "https://en.wikipedia.org/wiki/Main_Page"]
        return [scrapy.Request(url, self.parse, dont_filter=True) for url in urls]
    # allowed_domains = ["en.wikipedia.org"]
    # start_urls = [
    #             "http://en.wikipedia.org/wiki/Main_Page",
    #             "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]

    def parse(self, response):
        url = response.url
        title = response.css('h1 span::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))

    # def parse(self, response):
    #     item = Article()
    #     title = response.xpath('//h1/text()')[0].extract()
    #     print("Title is: "+title)
    #     item['title'] = title
    #     return item