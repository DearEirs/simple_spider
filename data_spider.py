# -*- coding: utf-8 -*-
import  requests
from lxml import etree
import time

from mysql_handler import mysql
from redis_handler import Redis_Handler
from config import header,xpaths


class Data_Spider(object):

    def __init__(self):
        self.header = header
        self.m = mysql()
        self.r = Redis_Handler()

    def get_url(self,name):
        """Get a url from redis where name = param's name 

        :param name: redis's set name 
        :return: :str:url
        """
        url = self.r.get_url(name)
        return url

    def open_url(self,url):
        """Open a url return it's html 

        :param url: URL which you want to open :
        :return: :str:html
        """
        html = requests.get(url=url,headers=self.header).content
        return html

    def get_data(self,html):
        h = etree.HTML(html)
        title = h.xpath(xpaths['title'])[0].encode('utf-8')
        content = h.xpath(xpaths['contents'])
        contents = ''
        for i in content:
            contents = contents + i
        contents = contents.encode('utf-8')
        return title,contents

    def save_data(self,*args):
        title,contents = args[0]
        self.m.table('Article').add({'title':title,'contents':contents})

    def start(self):
        url = self.get_url('contents_url')
        if not url:
            time.sleep(600)
        else:
            html = self.open_url(url)
            data = self.get_data(html)
            self.save_data(data)
            self.start()
