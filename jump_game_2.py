class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        jumps = 0
        index = 0
        next_index = 0
        for i in range(n):
            if i == index:
                index = max(A[i]+i, next_index)
                if i != n-1:
                    jumps += 1
            else:
                if A[i]+i > next_index:
                    next_index = A[i]+i

        return jumps

A = [2,3,1]
A = [0]
A = [1,1,1,1]
s = Solution()
print(s.jump(A))
