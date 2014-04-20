class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 2:
            return n
        index = 1
        count = 0
        for i in range(1, n):
            if A[i] != A[i-1]:
                A[index] = A[i]
                index += 1
                count = 0
            elif count == 0:
                A[index] = A[i]
                index += 1
                count += 1

        return index

a = [1,1,1,1,3,3]
s = Solution()
n = s.removeDuplicates(a)
print(a[0:n])
