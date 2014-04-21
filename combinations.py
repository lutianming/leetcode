class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if k == 0:
            return []
        if k == 1:
            return [[i] for i in range(1, n+1)]

        combinations = []
        for i, v in enumerate(range(n, k-1, -1)):
            subs = self.combine(n-i-1, k-1)
            for sub in subs:
                sub.append(v)
                combinations.append(sub)
        return combinations

s = Solution()
print(s.combine(4, 2))
