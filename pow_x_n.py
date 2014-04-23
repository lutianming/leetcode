class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1 if x >= 0 else -1

        if n == 1:
            return x

        sign = 1
        if n < 0:
            sign = -1
            n = -n
        half = n/2
        left = n % 2
        val = self.pow(x, half)
        val *= val
        if left:
            val *= x
        if sign == -1:
            val = 1./val
        return val

s = Solution()
print(s.pow(8.8, 3))
