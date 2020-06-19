from random import randint
from time import time, sleep


def down(filename):
    print('strat download:%s' % filename)
    time_to_download = randint(1,2)
    sleep(time_to_download)
    print('%sdownload finish! time:%ds:' % (filename, time_to_download))


def main():
    start = time()
    down('abdefg')
    down('gfedcba')
    end = time()
    print('finish total %2fs:' % (end-start))


if __name__ == '__main__':
    main()