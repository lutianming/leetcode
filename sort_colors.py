class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        n = len(A)
        left = 0
        right = n-1
        i = 0
        while i <= right and i >= left:
            v = A[i]
            if v == 0:
                if i == left:
                    i += 1
                    left += 1
                else:
                    A[i] = A[left]
                    A[left] = v
                    left += 1
            if v == 2:
                A[i] = A[right]
                A[right] = v
                right -= 1
            if v == 1:
                i += 1
        return A

a = [1, 2, 1, 0]
a = [0, 2, 1]
s = Solution()
print(s.sortColors(a))
