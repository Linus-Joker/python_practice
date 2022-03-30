class Search():
    def binary(self, data, input):
        data.sort()
        print("要尋找的數字:", input)
        print("排序後順序:", data)
        middle = int(len(data)/2)
        left = 0
        right = len(data)
        print("中間index:", middle)
        print("中間的數字:", data[middle])

        while (data[middle] != input):
            print("data[", middle, "]的數字=", data[middle], "是否等於", input)
            if left > right:
                break
            if input > data[middle]:
                left = middle + 1
            else:
                right = middle - 1
            middle = int((left+right)/2)
            # print("right更新為", right)
            # print("left更新為", left)
            # print("mid更新為", middle)
            if data[middle] == input:
                print("找到中間值:", data[middle])
                print("找到數字:", input)
            else:
                print("找到中間值:", data[middle])
                print("找不到數字:",  input)


data = [73, 50, 18, 67, 23, 67, 51, 27, 99, 45, 87, 1]
b = Search()
b.binary(data, 73)
