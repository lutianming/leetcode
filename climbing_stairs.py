class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        table = {}
        table[1] = 1
        table[2] = 2

        for i in range(1, n+1):
            if i not in table:
                table[i] = table[i-1] + table[i-2]

        return table[n]
s = 3
solution = Solution()
print(solution.climbStairs(s))
