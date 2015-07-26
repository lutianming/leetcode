class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        r = n
        count = 0
        while r:
            count += r % 2
            r = r / 2
        return count
