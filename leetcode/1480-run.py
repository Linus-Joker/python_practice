# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

    def addSum(self, n):
        for i in range(0, len(n)):
            n[i] = n[i] + 1
        return n


sul = Solution()

# print(sul.runningSum([1, 2, 3, 4]))
print(sul.addSum([1, 2, 3, 4]))
