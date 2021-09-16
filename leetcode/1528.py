from typing import List


def restoreString(s: str, indices: List[int]) -> str:
    res = [''] * len(s)

# 將indices[index]位置裡的數字指向新的res list位置
    for index, char in enumerate(s):
        res[indices[index]] = char
    return "".join(res)


print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
