class Solution:
    # @return a string
    def convert(self, s, nRows):
        n = len(s)
        if n <= 1:
            return s
        step = 2*(nRows-1)
        if step <= 0:
            return s
        zigzag = ''

        for i in range(0, n, step):
            zigzag += s[i]
        for i in range(1, nRows-1):
            for j in range(i, n, step):
                zigzag += s[j]
                k = j - j % step + (step - j % step)
                if k < n:
                    zigzag += s[k]
        for i in range(nRows-1, n, step):
            zigzag += s[i]
        return zigzag

s = Solution()
print(s.convert('ABCDE', 4))
