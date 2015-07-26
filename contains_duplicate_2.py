class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                j = d[num]
                if i - j <= k:
                    return True
                else:
                    d[num] = i
            else:
                d[num] = i
        return False
