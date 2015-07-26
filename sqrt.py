class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0:
            return 0

        sqrt = 1
        next_sqrt = x/2.0
        while abs(next_sqrt - sqrt) > 0.000001:
            sqrt = next_sqrt
            next_sqrt = (sqrt + x/sqrt) / 2.0
        return int(sqrt)

s = Solution()
print(s.mySqrt(2147395599))
