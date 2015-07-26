class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        # if len(s) == 1:
        #     return 1

        counts = []
        count = 0
        n = len(s)
        res = 1
        for i in range(n):
            if i+1 < n and 0 < int(s[i:i+2]) <= 26:
                count += 1
            else:
                if count != 0:
                    counts.append(count)
                    count = 0
        cache = {}
        cache[1] = 2
        cache[2] = 3
        for count in counts:
            res *= self.comb(cache, count)

        return res

    def comb(self, cache, count):
        if count not in cache:
            cache[count] = self.comb(cache, count-1) + self.comb(cache, count-2)
        return cache[count]


s = Solution()
print(s.numDecodings("0"))
print(s.numDecodings("12"))
