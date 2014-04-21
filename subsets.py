class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S = sorted(S)
        return self._subsets(S)

    def _subsets(self, S):
        n = len(S)
        if n == 0:
            return [[]]
        sets = []
        sub = self._subsets(S[0:n-1])
        for s in sub:
            sets.append(s)
            sets.append(s+[S[n-1]])
        return sets
