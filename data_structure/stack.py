# 初始list
stack = [3, 4, 5]


# 反轉list
# 取出list並重新放入新list
def reverse_stack(stack):
    new_stack = []
    for i in range(len(stack)):
        num = stack.pop()
        new_stack.append(num)

    return new_stack


def main():
    # 堆疊的增加
    stack.append(6)
    stack.append(7)
    print("堆疊共有%d筆數值:" % len(stack))
    print(stack)  # [3, 4, 5, 6, 7]

    new_stack = reverse_stack(stack)
    print("堆疊反轉後共有%d筆數值:" % len(new_stack))
    print(new_stack)  # [7,6,5,4,3]


if __name__ == '__main__':
    main()
