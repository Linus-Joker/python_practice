
from time import sleep
import time


def stars():
    for i in range(1, 4):
        print("*" * i)


stars()


def tower():
    for i in range(1, 8):
        print(' ' * (7-i) + '*' * (2*i-1))


# tower()

def diamond():
    for i in range(1, 8):
        print(' ' * (7-i) + '*' * (2*i-1))
    for i in range(7, 0, -1):
        print(' ' * (7-i) + '*' * (2*i-1))


# diamond()

def hidePassword(param):
    return '*' * len(param)


# param = input("input password:")
# print(hidePassword(param))

# print("%d"%123)

def add():
    a = 1
    b = 2
    c = 3
    result = a+b+c

    print("%d" % result)


# add()

def www():
    a = 1
    while(a < 20):
        if(a % 3 == 0 and a % 5 != 0):
            print("hi", a)
        a = a+1


# www()

def sum():
    sum = 0
    a = 1
    while(a < 101):
        sum = sum + a
        a = a + 1
    print(sum)


# sum()

def factorial():
    sum = 1
    a = 10
    while(a > 1):
        sum = sum * a
        a = a - 1
    print(sum)


# factorial()

def reciprocal():
    a = 10

    while(a > 1):
        print(a)
        sleep(1)
        a = a-1


# reciprocal()

def parallelStar():
    for i in range(0, 3):
        print("*****")


# parallelStar()

def judgmentPrime():
    a = 4

    while(a < 23):
        if(a % 2 == 0 or a % 3 == 0):
            print(a, "  is 合數")
        else:
            print(a, "  is 質數")
        a = a+1


# judgmentPrime()
def even():
    for i in range(0, 100, 2):
        print(i)


# even()

def tenThousand():
    # 時間開始
    time_start = time.time()

    # 跑1百萬次
    for i in range(0, 10**2):
        print("S123", i)

    # 時間結束
    time_end = time.time()

    time_c = time_end - time_start
    print(time_c, 's')


# 跑1百萬次
# tenThousand()
