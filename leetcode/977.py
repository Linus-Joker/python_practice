# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        b = []
        for i in range(len(A)):
            v = A[i] * A[i]
            b.append(v)
            b.sort()
        return b


sul = Solution()
print(sul.sortedSquares([-4, -1, 0, 3, 10]))

# 另外leetcode 的解法
# class Solution(object):
#     def sortedSquares(self, A):
#         return sorted(x*x for x in A)
