# 選擇排序法
# 先找到最大或最小的，再把它排到最左邊


def select_sort():
    nums = [12, 11, 10, 9, 13, 8]
    n = len(nums)
    # print(n)
    for i in range(len(nums)):
        min_idx = nums[i]
        # print(i)
        # print(min_idx)
        for j in range(i+1, n, 1):
            # print(j, nums[j])
            if nums[j] < min_idx:
                min_idx = nums[j]
                nums[i], nums[j] = nums[j], nums[i]
                # print(nums)
                # break
        print('目前是第', i+1, '次選擇排序:', nums)

# 找最小值(最大值就反過來)


# def min():
#     nums = [49, 57, 99, 23, 66]
#     for i in range(len(nums)):
#         min_idx = nums[i]
#         # print(min_idx)
#         for j in range(len(nums)):
#             # print(nums[j])
#             if nums[j] < min_idx:
#                 min_idx = nums[j]
#     print(min_idx)


select_sort()
# min()
