import redis
from config import redis_config

class Redis_Handler(object):

    def __init__(self):
        self.host = redis_config['host']
        self.passwd = redis_config['passwd']
        self.port = redis_config['port']
        self.__conn()

    def __conn(self):
        self.r = redis.Redis(host=self.host,port=self.port,password=self.passwd)
        return self


    def has_url(self,name,value):
        if self.r.sismember(name,value):
            return True
        else:
            return False

    def ins_url(self,name,*value):
        self.r.sadd(name,*value)

    def get_url(self,name):
        return  self.r.spop(name)

    def del_url(self,name,value):
        self.r.srem(name,value)

    def mv_url(self,s_name,d_name,value):
        self.r.smove(s_name,d_name,value)

    def smember(self,name,value=None):
        self.r.sismember(name,value)

    def diff(self,key1,*args):
        result = self.r.execute_command("SDIFF", key1, *args)
        return result
