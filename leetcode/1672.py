class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = 0
        for list in accounts:
            total = 0
            for i in range(len(list)):
                total = total + list[i]
                if total > result:
                    result = total
                    print(result)

        return(result)


s = Solution()
# s.maximumWealth([[1, 5], [7, 4], [9, 1]])
print(s.maximumWealth([[1, 5], [7, 4], [9, 1]]))
