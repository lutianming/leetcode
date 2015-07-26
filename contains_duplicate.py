class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = 1
        return False
