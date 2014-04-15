class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()
        tokens = s.split()
        tokens.reverse()
        return ' '.join(tokens)

s = "the sky is blue"
solution = Solution()
print(solution.reverseWords(s))
