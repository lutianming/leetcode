class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        m = len(a)
        n = len(b)
        if m > n:
            b = '0'*(m-n) + b
        else:
            a = '0'*(n-m) + a
        length = max(m, n)
        binary = ['']*length
        bit = 0
        for i in range(length-1, -1, -1):
            x = a[i]
            y = b[i]
            v = int(x) + int(y) + bit
            if v >= 2:
                bit = 1
                v -= 2
            else:
                bit = 0
            binary[i] = str(v)
        result = ''.join(binary)
        if bit == 1:
            result = '1' + result
        return result
