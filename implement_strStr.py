class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        if m < n:
            return None
        if m == n:
            if haystack == needle:
                return needle
            else:
                return None

        for i in range(m-n):
            result = True
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    result = False
                    break
            if result:
                break

        if result:
            return haystack[i:]
        else:
            return None

a = 'abcd'
b = 'bc'
s = Solution()
print(s.strStr(a, b))
