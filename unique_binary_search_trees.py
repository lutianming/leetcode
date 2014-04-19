class Solution:
    # @return an integer
    def numTrees(self, n):
        table = {}
        table[0] = 1
        table[1] = 1
        table[2] = 2
        return self._numTrees(n, table)

    def _numTrees(self, n, table):
        if n in table:
            return table[n]

        num = 0
        for i in range(n):
            num += self._numTrees(i, table) * self._numTrees(n-i-1, table)
        table[n] = num
        return num

n = 3
solution = Solution()
print(solution.numTrees(3))
