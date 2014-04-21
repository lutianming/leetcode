class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        jumps_left = 1
        result = True
        for a in A:
            if jumps_left:
                jumps_left -= 1
                if jumps_left < a:
                    jumps_left = a
            else:
                result = False
                break
        return result

A = [2,3,1,1,4]
B = [3,2,1,0,4]
s = Solution()
print(s.canJump(B))
