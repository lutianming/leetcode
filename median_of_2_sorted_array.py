class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if B is None or len(B) == 0:
            return self._findMedian(A)
        if A is None or len(A) == 0:
            return self._findMedian(B)
        m = len(A)
        n = len(B)
        if m == 1 and n == 1:
            return (A[0] + B[0])/2.0

        if m == 2 and n == 2:

        i = m/2
        j = n/2
        a_i = a[i]
        b_j = b[j]
        if a_i <= b_j:
            k = min(i, n-j-1)
            a = a[k:]
            b = b[:-k]
        else:
            k = min(m-i-1, j)
            a = a[:-k]
            b = b[k:]

    def _findMedian(self, A):
        n = len(A)
        if n % 2 == 0:
            return (A[n/2]+A[n/2-1])/2.0
        else:
            return A[n/2]
