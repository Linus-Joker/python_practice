# 堆疊的增加與取出

# 原本的list
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)  # [3, 4, 5, 6, 7]

# 反轉list
# 取出list並重新放入新list

new_stack = []
for i in range(len(stack)):
    num = stack.pop()
    new_stack.append(num)
print(new_stack)  # [7,6,5,4,3]
