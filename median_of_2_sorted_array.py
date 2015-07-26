class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if B is None or len(B) == 0:
            return self._findMedian(A)
        if A is None or len(A) == 0:
            return self._findMedian(B)

        if A[0] >= B[-1]:
            return self._findMedian(B+A)
        if B[0] >= A[-1]:
            return self._findMedian(A+B)

        m = len(A)
        n = len(B)
        if m == 1 and n == 1:
            return (A[0] + B[0])/2.0

        if m == 2 and n == 2:
            pass

        i = m/2
        j = n/2
        k = min(i, j)
        a_i = A[k]
        b_j = B[k]

        if a_i <= b_j:
            a = A[k+1:]
            b = B[0:k]
        else:
            a = A[0:k]
            b = B[k+1:]
        print(a, b)
        return self.findMedianSortedArrays(a, b)

    def _findMedian(self, A):
        n = len(A)
        if n % 2 == 0:
            return (A[n/2]+A[n/2-1])/2.0
        else:
            return A[n/2]

s = Solution()
print(s.findMedianSortedArrays([1,2], [1,2]))
