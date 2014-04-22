class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        count = 0
        subcount = 0
        high = 0
        index = 0
        for i in range(n):
            v = A[i]
            if v >= high:
                count += subcount
                subcount = 0
                index = i
                high = v
            else:
                subcount += high - v

        subcount = 0
        high = 0
        for i in range(n-1, index-1, -1):
            v = A[i]
            if v >= high:
                count += subcount
                subcount = 0
                index = v
                high = v
            else:
                subcount += high - v

        return count

a = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(a))
