class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        single = 0
        for a in A:
            single = single ^ a
        return single
