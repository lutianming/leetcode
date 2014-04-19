class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxsubsum = -float('Inf')
        subsum = -float('Inf')
        for i in A:
            if i > subsum and i > (subsum+i):
                subsum = i
            else:
                subsum += i
            if subsum > maxsubsum:
                maxsubsum = subsum
        return maxsubsum

s = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(s))
