# num = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
num = [33, 57, 11, 28, 77]


def bubble(data):
    n = len(data)
    for i in range(n-1):
        # 有 n 個資料長度，但只要執行 n-1 次
        # print(i)
        for j in range(n-1):
            # print(j)
            # 從第1個開始比較直到最後一個還沒到最終位置的數字
            if data[j] > data[j+1]:        # 比大小然後互換
                data[j], data[j+1] = data[j+1], data[j]
                print(data)


bubble(num)

# print(range(4))
