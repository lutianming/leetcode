class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse = 0
        r = n
        for i in range(32):
            bit = r % 2
            reverse += bit << (32-i-1)
            r = r / 2
        return reverse

s = Solution()
r = s.reverseBits(43261596)
print(r)
