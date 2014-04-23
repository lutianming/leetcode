class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
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
            if target % candidates[0] == 0:
                v = candidates[0]
                c = target / candidates[0]
                combines.append([v]*c)
            return combines

        subs = self._combine(candidates[:-1], target)
        combines.extend(subs)
        for sub in self._combine(candidates, target-candidates[-1]):
            sub.append(candidates[-1])
            combines.append(sub)
        return combines

a = [2,3,6,7]
a = [1,2]
s = Solution()
print(s.combinationSum(a, 2))
