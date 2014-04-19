class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower()
        n = len(s)
        i = 0
        j = n-1
        is_pal = True
        while i <= j:
            left = s[i]
            right = s[j]
            if left.isalnum() and right.isalnum():
                if left != right:
                    is_pal = False
                    break
                else:
                    i += 1
                    j -= 1
            else:
                if not left.isalnum():
                    i += 1
                if not right.isalnum():
                    j -= 1
        return is_pal

a = 'a.'
a = '8V8K;G;K;V;'
s = Solution()
print(s.isPalindrome(a))
