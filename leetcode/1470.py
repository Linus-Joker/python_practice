# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        b = []

        for i in range(0, n):
            v = nums.pop(0)
            b.append(v)
            n -= 1
            l = nums.pop(n)
            b.append(l)
        return b


sul = Solution()
print(sul.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
