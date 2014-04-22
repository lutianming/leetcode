class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        bound = {}
        maxbound = 0
        for n in num:
            if n not in bound:
                bound[n] = 1
                if n-1 in bound:
                    leftbound = bound[n-1]
                else:
                    leftbound = 0

                if n+1 in bound:
                    rightbound = bound[n+1]
                else:
                    rightbound = 0

                bound[n-leftbound] = bound[n+rightbound] = 1+leftbound+rightbound
                maxbound = max(maxbound, 1+leftbound+rightbound)
        return maxbound

a = [100, 4, 200, 1, 3, 2]
s = Solution()
print(s.longestConsecutive(a))
