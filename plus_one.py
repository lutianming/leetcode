class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        n = len(digits)
        bit = 1
        for i in range(n-1, -1, -1):
            digit = digits[i]
            digit += bit
            if digit == 10:
                digit = 0
                bit = 1
            else:
                bit = 0
            digits[i] = digit
        if bit == 1:
            digits.insert(0, bit)
        return digits
