# 階成練習-動態規劃-Fibonacci

f = []


def n_count():
    f.append(1)
    f.append(1)

    for i in range(2, 11, 1):
        f.append(f[i-1] + f[i-2])
        print(f)


# print(n_count())
n_count()
