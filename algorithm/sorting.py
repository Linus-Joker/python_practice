def select_sort():
    y = [23, 55, 33, 16]
    for i in range(len(y)):
        min_idx = y[i]
        for j in range(i, len(y)-1, 1):
            if y[j] < min_idx:
                min_idx = y[j]
                y[i], y[j] = y[j], y[i]
        print(y)

# 找最小值(最大值就反過來)


def min():
    y = [49, 57, 99, 23, 66]
    for i in range(len(y)):
        min_idx = y[i]
        # print(min_idx)
        for j in range(len(y)):
            # print(y[j])
            if y[j] < min_idx:
                min_idx = y[j]
    print(min_idx)


select_sort()
# min()
