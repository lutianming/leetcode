class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        current = None
        count = 0
        for num in nums:
            if num != current:
                count -= 1
                if count < 0:
                    current = num
                    count = 1
            else:
                count += 1
        return current
