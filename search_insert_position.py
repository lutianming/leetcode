class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i, v in enumerate(A):
            if target <= v:
                return i
        return i+1
