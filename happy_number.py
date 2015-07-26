class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        nums = []
        while n not in nums:
            nums.append(n)
            next_n = sum([int(d)*int(d) for d in str(n)])
            if next_n == 1:
                return True
            n = next_n
        return False
