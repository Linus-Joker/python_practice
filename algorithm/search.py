y = [49, 57, 99, 23, 66]


def search(data):
    n = len(data)
    num = int(23)
    for i in range(n):
        if num == data[i]:
            print(num)


search(y)
