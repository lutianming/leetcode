class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        max_length = 0
        max_left = 0
        max_right = 0
        n = len(s)
        for i, c in enumerate(s):
            left = None
            right = None

            if (i-1) >= 0 and c == s[i-1]:
                left = i-1
                right = i

                while left >= 0 and right < n:
                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else:
                        break

                length = right-left-2 + 1
                if max_length < length:
                    max_length = length
                    max_left = left+1
                    max_right = right-1

            if (i-2) >= 0 and c == s[i-2]:
                left = i-2
                right = i

                while left >= 0 and right < n:
                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else:
                        break

                length = right-left-2 + 1
                if max_length < length:
                    max_length = length
                    max_left = left+1
                    max_right = right-1

        return s[max_left:max_right+1]


s = Solution()
# print(s.longestPalindrome("a"))
print(s.longestPalindrome("aaaa"))
# print(s.longestPalindrome("abcb"))
