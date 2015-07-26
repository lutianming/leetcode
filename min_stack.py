class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if self.stack:
            m = self.stack[-1][1]
            if m > x:
                self.stack.append((x, x))
            else:
                self.stack.append((x, m))
        else:
            self.stack.append((x, x))

    # @return nothing
    def pop(self):
        self.stack.pop()

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            None

    # @return an integer
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            None
