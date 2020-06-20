from random import randint
from threading import Thread
from time import time, sleep


class Down(Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        print('start download:%s' % self.filename)
        time_to_download = randint(1, 2)
        sleep(time_to_download)
        print('%sdownload finish!! time:%ds' % (self.name, time_to_download))


def main():
    try:
        start = time()
        t1 = Down('ABCDEFG')
        t1.start()
        t1.join()
    except:
        print('error')


if __name__ == '__main__':
    main()
