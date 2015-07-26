class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        n = 0
        for c in s:
            i = ord(c) - ord("A") + 1
            n = n*26 + i
        return n

s = Solution()
print(s.titleToNumber('AA'))
