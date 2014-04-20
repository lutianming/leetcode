class Solution:
    # @return a string
    def intToRoman(self, num):
        s = ''
        for i in range(3, -1, -1):
            d = num/(10**i)
            d = d % 10
            if i == 3:
                s += 'M'*d
            elif i == 2:
                c = self.digit(d, 'M', 'D', 'C')
                s += c
            elif i == 1:
                c = self.digit(d, 'C', 'L', 'X')
                s += c
            elif i == 0:
                c = self.digit(d, 'X', 'V', 'I')
                s += c
        return s

    def digit(self, v, high, middle, low):
        if v <= 3:
            return low*v
        elif v <= 5:
            s = low*(5-v) + middle
        elif v <= 8:
            s = middle + low*(v-5)
        else:
            s = low*(10-v) + high
        return s

s = Solution()
print(s.intToRoman(13))
