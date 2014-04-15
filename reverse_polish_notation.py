class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        ops = ['+', '-', '*', '/']
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    c = a + b
                elif token == '-':
                    c = a - b
                elif token == '*':
                    c = a * b
                elif token == '/':
                    c = int(float(a)/b)
                stack.append(c)
            else:
                stack.append(int(token))
        return stack.pop()


a = ["2", "1", "+", "3", "*"]   #9
b = ["4", "13", "5", "/", "+"]  #6
c = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
s = Solution()
print(s.evalRPN(a))
print(s.evalRPN(b))
print(s.evalRPN(c))
