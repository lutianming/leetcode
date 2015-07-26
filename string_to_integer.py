class Solution:
    def myAtoi(self, str):
        if len(str) == 0:
            return 0

        res = 0
        max_int = 2147483647
        min_int = -2147483648

        for i in range(0, len(str)):
            c = str[i]
            if c != ' ':
                break

        s = str[i:]
        pos = False
        if s[0] == '-':
            pos = False
            s = s[1:]
        elif s[0] == '+':
            pos = True
            s = s[1:]
        else:
            pos = True
            s = s

        for c in s:
            if c >= '0' and c <= '9':
                res = res*10 + int(c)
            else:
                break
        if not pos:
            res = -res
        if res > max_int:
            res = max_int
        if res < min_int:
            res = min_int
        return res

a = Solution()
r = a.myAtoi("")
print(r)
r = a.myAtoi("  ab")
print(r)
r = a.myAtoi("  -123")
print(r)
