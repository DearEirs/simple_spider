mysql_config = {
    'host':'host',
# Last Change:  2017-05-10 18:11:50
    'user':'root',
    'passwd':'passwd',
    'port':3306,
    'db':'dbname',
    'prefix':'prefix',
    'charset':'utf8'
}

redis_config = {
    'host': 'host',
    'passwd': 'passwd',
    'port': '6379',
}

# You can add more if you want.
header =  {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

# For example
xpaths = {
    'title':'//*[@id="wrapper"]/div[3]/div[2]/h1/text()',
    'contents':'//*[@id="content"]/text()',
    'pre_url':'//*[@id="wrapper"]/div[3]/div[2]/div[4]/li[1]/a/@href',
    'next_url':'//*[@id="wrapper"]/div[3]/div[2]/div[4]/li[3]/a/@href',
    'all_urls':'//a/@href',
}
