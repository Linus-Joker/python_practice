def f(n):
    if (n == 1):
        re = 1
    else:
        re = n*f(n-1)
    print(n, "階乘等於", re)
    return re


n = int(input("請輸入N值？"))
result = f(n)
print(n, "階乘等於", result)
