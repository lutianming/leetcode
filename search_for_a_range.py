class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        n = len(A)
        low = 0
        high = n-1
        left = -1
        right = -1
        while low <= high:
            middle = low + (high-low)/2
            v = A[middle]
            if target == v:
                left = self.left_bound(A, middle)
                right = self.right_bound(A, middle)
                break
            elif target > v:
                low = middle+1
            else:
                high = middle-1
        return [left, right]

    def left_bound(self, A, i):
        j = i-1
        while j >= 0 and A[j] == A[i]:
            j -= 1
        return j+1

    def right_bound(self, A, i):
        j = i+1
        n = len(A)
        while j < n and A[j] == A[i]:
            j += 1
        return j-1

a = [5, 7, 7, 8, 8, 10]
s = Solution()
print(s.searchRange(a, 8))
