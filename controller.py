from gevent import monkey; monkey.patch_all()
import gevent
from multiprocessing import Process

from data_spider import Data_Spider
from url_spider import Url_Spider

def main():
    u = Url_Spider()
    d = Data_Spider()
    func_list = [u.start,d.start]
    gevent.joinall([gevent.spawn(func) for func in func_list])

if __name__ == '__main__':
    for i in range(3):
        p = Process(target=main)
        p.start()
