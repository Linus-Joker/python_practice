# 初始list
queue = [3, 4, 5]


# 取出list並重新放入新list
def get_queue(queue):
    new_queue = []
    for i in range(len(queue)):
        num = queue.pop(0)
        new_queue.append(num)

    # print(len(new_queue))
    return new_queue


def main():
    queue.append(6)
    queue.append(7)
    print("佇列共有%d筆數值:" % len(queue))
    print(queue)  # [3, 4, 5, 6, 7]

    new_queue = get_queue(queue)
    print("重新放入佇列後共有%d筆數值:" % len(new_queue))
    print(new_queue)  # [3, 4, 5, 6, 7]


if __name__ == '__main__':
    main()
