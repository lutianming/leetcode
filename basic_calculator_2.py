class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        n = len(s)

        res = 0
        term = None
        op = None

        i = 0
        while i < n:
            c = s[i]

            if c.isdigit():
                (term, i) = self.next_int(s, i)
            elif c == ' ':
                i += 1
            else:
                if c == '+' or c == '-':
                    res = self.do_calculate(res, term, op)
                    op = c
                    i += 1
                if c == '*' or c == '/':
                    (tmp, i) = self.next_int(s, i+1)
                    term = self.do_calculate(term, tmp, c)

        return self.do_calculate(res, term, op)

    def next_int(self, s, i):
        number = ""
        n = len(s)
        while i < n:
            c = s[i]
            if c.isdigit():
                number = number + c
            elif c == ' ':
                pass
            else:
                break
            i += 1
        return (int(number), i)

    def do_calculate(self, left, right, op):
        if not right:
            return left
        if op == '+':
            res = left + right
        elif op == '-':
            res = left - right
        elif op == '*':
            res = left * right
        elif op == '/':
            res = left / right
        else:
            res = left + right
        return res



s = Solution()
print(s.calculate("3+2*2"))
print(s.calculate(" 3/2 "))
print(s.calculate(" 3+5 / 2 "))
