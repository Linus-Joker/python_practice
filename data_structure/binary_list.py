def Btree_create(btree, data, length):
    for i in range(1, length):
        level = 1
        while btree[level] != 0:
            if data[i] > btree[level]:  # 如果陣列內的值大於樹根，則往右子樹比較
                level = level*2+1
            else:  # 如果陣列內的值小於或等於樹根，則往左子樹比較
                level = level*2
        btree[level] = data[i]  # 把陣列值放入二元樹


length = 7
# data = [0, 6, 3, 5, 4, 7, 8, 9, 2]
data = [0, 5, 4, 6, 2, 1, 8, 3, 7]
btree = [0]*40
Btree_create(btree, data, 9)

for i in range(1, 16):
    print(btree[i])
