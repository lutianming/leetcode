class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        m = len(num1)
        n = len(num2)
        if m > n:
            m, n = n, m
            num1, num2 = num2, num1
        s = ''
        cache = {}
        for i in range(n):
            tmp = ''
            bit = 0
            mul = int(num2[n-i-1])
            if mul == 0:
                tmp = '0'
            elif mul == 1:
                tmp = num1
            elif mul in cache:
                tmp = cache[mul]
            else:
                for j in range(m):
                    v = int(num1[m-j-1]) * mul + bit
                    bit = v / 10
                    v = v % 10
                    tmp = str(v) + tmp
                if bit > 0:
                    tmp = str(bit)+tmp
                cache[mul] = tmp
            tmp += '0'*i
            s = self.add(s, tmp)
        return s

    def add(self, num1, num2):
        m = len(num1)
        n = len(num2)
        l = max(m, n)
        if m < n:
            num1 = '0'*(n-m) + num1
        else:
            num2 = '0'*(m-n) + num2

        s = ''
        bit = 0
        for i in range(l):
            v = int(num1[l-i-1]) + int(num2[l-i-1]) + bit
            bit = v / 10
            v = v % 10
            s = str(v) + s
        if bit:
            s = '1'+s
        return s

num1 = '9369162965141127216164882458728854782080715827760307787224298083754'
num2 = '7204554941577564438'
s = Solution()
print(s.multiply(num1, num2))
