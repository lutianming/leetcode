class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = 0
        currm = m
        for j in range(n):
            b = B[j]
            while i < m+n:
                if i < currm:
                    if b <= A[i]:
                        A.insert(i, b)
                        currm += 1
                        i += 1
                        break
                    i += 1
                else:
                    A[currm] = b
                    currm += 1
                    i = currm
                    break

A = [1,0]
B = [2,0]
A = [4,5,6, 0, 0, 0]
B = [1,2,3]
s = Solution()
s.merge(A, 3, B, 3)
print(A[0:6])
