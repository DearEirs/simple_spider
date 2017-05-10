#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib,urllib2,json,sys,time,datetime
from collections import Counter
import operator

reload(sys)
sys.setdefaultencoding( "utf-8" )

yes_time=datetime.date.fromtimestamp(time.time()) + datetime.timedelta(days=-1)

ip_list = []
ip_data = []
dir_list=[]
dir_data=[]
data = []

class WeChat(object):
        __token_id = ''

        # init attribute
        def __init__(self, url):
                self.__url = url.rstrip('/')
                self.__corpid = 'wx30fa7b30bac3337e'
                self.__secret = 'CyPiAQ435TzT84uRvo29NrBx2u6IJ9gD2BWSbsTDzVOrU_zKhUwl4Njdc--y57Jb'

        # Get TokenID
        def authID(self):
                params = {'corpid': self.__corpid, 'corpsecret': self.__secret}
                data = urllib.urlencode(params)

                content = self.getToken(data)

                try:
                        self.__token_id = content['access_token']
                        # print content['access_token']
                except KeyError:
                        raise KeyError

        # Establish a connection
        def getToken(self, data, url_prefix='/'):
                url = self.__url + url_prefix + 'gettoken?'
                try:
                        response = urllib2.Request(url + data)
                except KeyError:
                        raise KeyError
                result = urllib2.urlopen(response)
                content = json.loads(result.read())
                return content

        # Get sendmessage url
        def postData(self, data, url_prefix='/'):
                url = self.__url + url_prefix + 'messagend?access_token=%s' % self.__token_id
                request = urllib2.Request(url, data)
                try:
                        result = urllib2.urlopen(request)
                except urllib2.HTTPError as e:
                        if hasattr(e, 'reason'):
                                print 'reason', e.reason
                        elif hasattr(e, 'code'):
                                print 'code', e.code
                        return 0
                else:
                        content = json.loads(result.read())
                        result.close()
                return content

        # send message
        def sendMessage(self, touser, message):

                self.authID()

                data = json.dumps({
                        'touser': touser,
                        'toparty': "2",
                        'msgtype': "text",
                        'agentid': "2",
                        'text': {
                                'content': message
                        },
                        'safe': "0"
                }, ensure_ascii=False)

                response = self.postData(data)
                print response
def ip_ipadder(ip):
    url = 'http://freeapi.ipip.net/%s'%ip
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    content = resp.read()
    return content

if __name__ == '__main__':
        with open('/datainx/log/access_20160902_bak.log', 'r') as f_log:
                for i in f_log.readlines():
                        ip_list.append(i.split(" ")[0])
                        dir_list.append(i.split(" ")[6])                   
        ip_list = sorted(dict(Counter(ip_list)).items(), key=lambda x: x[1], reverse=True)[0:10]
        for i in ip_list:
            ip_res = ip_ipadder(i[0]).split('"')
            ipadder = '%s-%s-%s-%s' % (ip_res[1], ip_res[3], ip_res[5], ip_res[9])
            data.append('ip:%s,访问次数:%s,地址:%s' % (i[0], i[1], ipadder))
            time.sleep(1)
        d='\n'.join(tuple(data))

        dir_list = sorted(dict(Counter(dir_list)).items(), key=lambda x: x[1], reverse=True)[0:10]
        for i in dir_list:
                dir_data.append('访问路径:%s,访问次数:%s' % (i[0], i[1]))
        d2 = '\n'.join(tuple(dir_data))

        a = WeChat('https://qyapi.weixin.qq.com/cgi-bin 

')
        a.sendMessage('wen_jie', str(yes_time)+'前十名访问日志\n'+d+'\n\n\n'+d2)
