
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        title = ''
        a = ord('A')
        while True:
            n = n - 1
            r = n % 26
            c = chr(a+r)
            title = c + title
            n = n / 26
            if n == 0:
                break
        return title

s = Solution()
print(s.convertToTitle(26))
