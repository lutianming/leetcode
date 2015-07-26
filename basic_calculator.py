class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        stack = []
        stack.append(0)
        stack.append('+')
        number = ""
        val = None
        brackets = 0

        n = len(s)
        for i in range(n):
            c = s[i]
            if c.isdigit():
                number = number + c
            else:
                if len(number) > 0:
                    self.do_calculate(stack, number)
                    number = ""

                if c == '(':
                    stack.append(c)
                    stack.append(0)
                    stack.append('+')

                if c == ')':
                    res = stack.pop()
                    stack.pop() # '('
                    self.do_calculate(stack, res)

                if c == '+':
                    stack.append(c)
                if c == '-':
                    stack.append(c)

        if len(number) > 0:
            self.do_calculate(stack, number)

        return stack.pop()

    def do_calculate(self, stack, number):
        if len(stack) > 0:
            op = stack.pop()
        else:
            op = '+'

        if op == '+':
            res = stack.pop() + int(number)
        elif op == '-':
            res = stack.pop() - int(number)

        stack.append(res)

s = Solution()
print(s.calculate("1 + 1"))
print(s.calculate(" 2-1 + 2 "))
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
