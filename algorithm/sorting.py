#選擇排序法
def select_sort():
    y = [12 ,11, 10]
    n = len(y)
    for i in range(len(y)):
        min_idx = y[i]
        print(min_idx)
        for j in range(i, n, 1):
            print(j, y[j])
            if y[j] < min_idx:
                # min_idx = y[j]
                y[i], y[j] = y[j], y[i]
                # print(y[i], y[j])
        # print('目前是第', i+1, '次選擇排序:', y)

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
