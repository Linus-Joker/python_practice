# 堆疊的增加與取出

# 原本的list

queue = [3, 4, 5]
queue.append(6)
queue.append(7)
print(queue)  # [3, 4, 5, 6, 7]

# 取出list並重新放入新list
new_queue = []
for i in range(len(queue)):
    num = queue.pop(0)
    new_queue.append(num)

print(new_queue)  # [3, 4, 5, 6, 7]
