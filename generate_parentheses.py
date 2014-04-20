class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        return self._generate(n, n)

    def _generate(self, left, right):
        if left == 0:
            return [')'*right]

        if left == right:
            sub = self._generate(left-1, right)
            return ['('+s for s in sub]
        if left < right:
            sub1 = self._generate(left-1, right)
            sub1 = ['('+s for s in sub1]
            sub2 = self._generate(left, right-1)
            sub2 = [')'+s for s in sub2]
            return sub1 + sub2

n = 3
s = Solution()
print(s.generateParenthesis(n))
