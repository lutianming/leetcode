class Solution:
    # @return an integer
    def romanToInt(self, s):
        val = 0

        for c in s:
            if c == 'I':
                val += 1
            elif c == 'V':
                val = self.add(val, 5)
            elif c == 'X':
                val = self.add(val, 10)
            elif c == 'L':
                val = self.add(val, 50)
            elif c == 'C':
                val = self.add(val, 100)
            elif c == 'D':
                val = self.add(val, 500)
            elif c == 'M':
                val = self.add(val, 1000)
            else:
                pass
        return val

    def add(sefl, val, v):
        if val % v != 0:
            val += v - (val % v)*2
        else:
            val += v
        return val
