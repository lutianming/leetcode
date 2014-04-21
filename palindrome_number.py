class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        digit = 0
        while x / (10**digit) != 0:
            digit += 1
        digit -= 1

        i = 0
        j = digit
        result = True
        while i < j:
            v1 = (x / (10**i)) % 10
            v2 = (x / (10**j)) % 10
            if v1 != v2:
                result = False
                break
            i += 1
            j -= 1
        return result
