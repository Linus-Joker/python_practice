# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        for i in range(0, len(A)):
            v = A.pop()
            B.append(v)
        return B

    def B(self, A):
        a1 = []
        a2 = []
        for i in A:
            if i % 2 == 0:
                a1.append(i)
            else:
                a2.append(i)
        return a1 + a2


sol = Solution()
# print(sol.sortArrayByParity([3, 1, 2, 4]))
print(sol.B([3, 1, 2, 4]))
