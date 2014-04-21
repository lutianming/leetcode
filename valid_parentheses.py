class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        valid = True
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if c in [')', '}', ']']:
                    if len(stack) > 0:
                        p = stack.pop()
                        if c == ')' and p != '(':
                            valid = False
                            break
                        elif c == '}' and p != '{':
                            valid = False
                            break
                        elif c == ']' and p != '[':
                            valid = False
                            break
                    else:
                        valid = False
                        break
        if len(stack) > 0:
            valid = False
        return valid
