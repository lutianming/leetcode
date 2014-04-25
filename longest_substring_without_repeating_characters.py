class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        substring = ''
        length = 0
        for c in s:
            if c not in substring:
                substring += c
            else:
                length = max(len(substring), length)
                i = substring.index(c)
                substring = substring[i+1:] + c
        length = max(len(substring), length)
        return length

a = "abcabcbb"
a = 'bbb'
a = "qopubjguxhxdipfzwswybgfylqvjzhar"
s = Solution()
print(s.lengthOfLongestSubstring(a))
