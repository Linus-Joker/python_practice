# nums = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
nums = [33, 28, 77, 56, 11]
n = len(nums)


class Sort():

    def bubble(self, nums):
        print("原始資料:", nums)
        # 有n個資料，泡沫排序將最大值移往最後，所以執行n-1次
        for i in range(n-1):
            for j in range(n-1):
                # 比大小後互換
                # > 則從大到小，< 則從小到大
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            print("第", i+1, "排序次數:", nums)
        print("排序結果:", nums)


s = Sort()

s.bubble(nums)
