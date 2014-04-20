class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n < 0:
            return []
        if n == 0:
            return [0]
        subcodes = self.grayCode(n-1)
        codes = []
        for i, code in enumerate(subcodes):
            code = code << 1
            if i % 2 == 0:
                codes.append(code)
                codes.append(code+1)
            else:
                codes.append(code+1)
                codes.append(code)

        return codes
