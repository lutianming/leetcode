class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length <= 1:
            return length
        index = 1
        for i in range(1, length):
            if A[i] != A[i-1]:
                A[index] = A[i]
                index += 1
        return index
