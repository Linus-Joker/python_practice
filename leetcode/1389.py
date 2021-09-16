from typing import List

'''
Example1:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
'''

'''
@param list[] nums
@param list[] index
@return list target
'''


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target


s = Solution()
print(s.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
