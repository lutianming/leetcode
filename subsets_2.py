class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S = sorted(S)
        return self._subsets(S)

    def _subsets(self, S):
        n = len(S)
        if n == 0:
            return [[]]
        sets = []
        sub = self._subsets(S[0:n-1])
        for s in sub:
            if s not in sets:
                sets.append(s)
            t = s+[S[n-1]]
            if t not in sets:
                sets.append(t)
        return sets
