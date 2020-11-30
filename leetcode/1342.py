class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 0
        while (num > 0):
            i += 1
            if (num % 2 == 0):
                num = num / 2
            else:
                num -= 1
        return i


sol = Solution()
print(sol.numberOfSteps(123))
