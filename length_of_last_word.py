class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        new = False
        for c in s:
            if c == ' ':
                new = True
            else:
                if new:
                    length = 1
                    new = False
                else:
                    length += 1
        return length
