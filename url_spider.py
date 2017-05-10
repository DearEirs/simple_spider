from urllib2 import  urlopen
from lxml import etree
import random

from redis_handler import Redis_Handler
from config import xpaths

class Url_Spider(object):

    def __init__(self,):
        self.r  = Redis_Handler()

    def open_url(self,url):
        html = urlopen(url).read().decode('gbk')
        return html

    def get_urls(self,html):
        h = etree.HTML(html)
        urls = h.xpath(xpaths['all_urls'])
        return urls

    def ins_urls(self,urls,name):
        for url in urls:
            if url == '/' or 'ddbiquge' not in url:
                continue
            else:
                if  'http' not  in url:
                    url = 'http://www.ddbiquge.com'+url
                if not self.r.has_url('all_urls',url):
                    self.r.ins_url('all_urls',url)
                    if 'chapter' in url and not self.r.has_url('contents',url):
                        self.r.ins_url('contents',url)

    def start(self,start_url=None):
        if not start_url:
            start_url = list(self.r.diff('all_urls','scaned_urls'))[0]
        if not self.r.diff('all_urls','scaned_urls'):
            return
        html = self.open_url(start_url)
        urls = self.get_urls(html)
        self.ins_urls(urls,'all_urls')
        self.r.ins_url('scaned_urls',start_url)
        self.start(list(self.r.diff('all_urls','scaned_urls'))[random.randint(1,5)])


if __name__ == '__main__':
    start_url = 'http://www.ddbiquge.com'
    url_spider = Url_Spider()
    url_spider.start(start_url)
