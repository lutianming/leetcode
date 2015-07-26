class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        res = m
        index = 0
        v = m
        res = 0
        while v:
            r = v % 2
            if r:
                limit = 1 << (index+1)
                if limit > n:
                    res += 1 << index
            v = v / 2
            index += 1
        return res

s = Solution()
print(s.rangeBitwiseAnd(5, 7))
