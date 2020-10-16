y = [49, 57, 99, 23, 66]


def search(data):
    data.sort()
    # print(data)
    n = len(data)
    num = int(23)
    for i in range(n):
        if num == data[i]:
            print("找到的數字:", num)
        else:
            print("未找到數字!!")


search(y)
