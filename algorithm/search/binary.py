# test
score = [45, 59, 62, 67, 70, 78, 83, 85, 88, 92, 96]
mid = 5
left = 0
right = len(score) - 1
while (score[mid] != 59):
    print("檢查score[", mid, "]=", score[mid], "是否等於62")
    if left >= right:
        break
    if score[mid] > 59:
        right = mid-1
    else:
        left = mid+1
    mid = int((left+right)/2)
    print("right更新為", right)
    print("left更新為", left)
    print("mid更新為", mid)
    if score[mid] == 62:
        print("找到62分")
    else:
        print("找不到62分")


# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def binary_search(data, key):
#     #設置選取範圍的指標
#     low = 0
#     upper = len(data) - 1
#     while low <= upper:
#         mid = (low + upper) / 2  #取中間索引的值
#         if data[mid] < key:    #若搜尋值比中間的值大，將中間索引+1，取右半
#             low = mid + 1
#         elif data[mid] > key:  #若搜尋值比中間的值小，將中間索引+1，取左半
#             upper = mid - 1
#         else:                    #若搜尋值等於中間的值，則回傳
#             return mid
#     return -1


# index = binary_search(data, 5)
# if index >= 0:
#     print("找到數值於索引 " + str(index))
# else:
#     print("找不到數值")
