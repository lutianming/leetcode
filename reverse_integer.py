class Solution:
    # @return an integer
    def reverse(self, x):
        if x >= 0:
            op = 1
        else:
            op = -1
        x = abs(x)
        val = 0
        while x != 0:
            digit = x % 10
            val *= 10
            val += digit
            x = x / 10
        val *= op
        return val
