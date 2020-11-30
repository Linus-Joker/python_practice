# 遞迴法-Fibonacci


def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])


# print(sum([5, 7, 3, 8, 10]))


def factorial(n):
    print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
# 個人結論是5*4*3*2*1，先重複跑factorial函式，將值先代回來，當n=0時結束並return 值回來


print(factorial(5))


def f(n):

    if n == 1 or n == 2:
        return 1
    else:
        count = 0
        count += 1
        # print(count)
        return f(n - 1) + f(n - 2)


# 這裡的結果是指index
# for i in range(1, 11):
#     print(i, ":", f(i))
