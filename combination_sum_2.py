class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        c = sorted(candidates)
        return self._combine(c, target)

    def _combine(self, candidates, target):
        combines = []
        if target < 0:
            return combines
        if target == 0:
            combines.append([])
            return combines

        n = len(candidates)
        if n <= 0:
            return combines
        if n == 1:
            if target == candidates[0]:
                v = candidates[0]
                combines.append([v])
            return combines

        subs = self._combine(candidates[:-1], target)
        combines.extend(subs)
        for sub in self._combine(candidates[:-1], target-candidates[-1]):
            sub.append(candidates[-1])
            if sub not in combines:
                combines.append(sub)
        return combines

a = [10,1,2,7,6,1,5]
s = Solution()
print(s.combinationSum2(a, 8))
