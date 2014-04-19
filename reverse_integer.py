class Solution:
    # @return an integer
    def reverse(self, x):
        if x >= 0:
            op = 1
        else:
            op = -1
        x = abs(x)
        s = str(x)
        n = len(str(x))
        val = 0
        for i in range(n):
            val += int(s[i]) * 10**(i)
        val *= op
        return val
