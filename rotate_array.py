class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        size = len(nums)
        step = k % size
        if step == 0:
            return
        a = nums[-step:]
        b = nums[0:-step]
        nums[0:step] = a
        nums[step:] = b

s = Solution()
nums = [1]
s.rotate(nums, 0)
print(nums)
