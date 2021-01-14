# def Merge_Sort(array):
#     if len(array) > 1:
#         mid = len(array) // 2
#         left_array = array[:mid]
#         right_array = array[mid:]
#         Merge_Sort(left_array)
#         Merge_Sort(right_array)
#         right_index = 0
#         left_index = 0
#         merged_index = 0

#         while right_index < len(right_array) and left_index < len(left_array):
#             if(right_array[right_index] < left_array[left_index]):
#                 array[merged_index] = right_array[right_index]
#                 right_index = right_index + 1
#             else:
#                 array[merged_index] = left_array[left_index]
#                 left_index = left_index + 1
#             merged_index = merged_index + 1

#         while right_index < len(right_array):
#             array[merged_index] = right_array[right_index]
#             right_index = right_index + 1
#             merged_index = merged_index + 1

#         while left_index < len(left_array):
#             array[merged_index] = left_array[left_index]
#             left_index = left_index + 1
#             merged_index = merged_index + 1


# Numbers = [41, 33, 17, 80, 61, 5, 55]
# Merge_Sort(Numbers)
# print(Numbers)

# ----------------------

# def merge(nb1, nb2):
#     if len(nb1) == 0:
#         return nb2
#     elif len(nb2) == 0:
#         return nb1
#     elif nb1[0] < nb2[0]:
#         return [nb1[0]] + merge(nb1[1:], nb2)
#     else:
#         return [nb2[0]] + merge(nb1, nb2[1:])


# number1 = [13, 4, 35, 5, 2]
# number2 = [8, 11, 3, 26, 14]
# number1.sort()
# number2.sort()
# print(merge(number1, number2))

import random
from collections import deque

unsortData = random.sample(range(100), 10)


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            # deque popleft is also O(1)
            merged.append(
                left.popleft() if left[0] <= right[0] else right.popleft())
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(lst) // 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)


print("Original Data:", unsortData)
sortData = merge_sort(unsortData)
print("Sorted Data:", sortData)
