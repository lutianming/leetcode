class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i, num in enumerate(nums[2:]):
            i = i+2
            dp[i] = max(dp[i-1], dp[i-2]+num)
        return dp[n-1]

s = Solution()
res = s.rob([1,1,1])
print(res)
