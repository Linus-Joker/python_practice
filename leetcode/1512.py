# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
from collections import Counter
from itertools import combinations_with_replacement


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        n = 0
        length = len(nums)
        for i in range(0, length):
            n += 1
            for j in range(n, length):
                if nums[i] == nums[j]:
                    x += 1
        print(x)


sol = Solution()
sol.numIdenticalPairs([1, 2, 3, 1, 1, 3])
