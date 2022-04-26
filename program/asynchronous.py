from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('啟動下載，號碼[%d].' % getpid())
    print('開始下載%s...' % filename)
    time_to_download = randint(1, 2)
    sleep(time_to_download)
    print('%s下載完成! 共花費%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python從入門到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('總共耗費了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
