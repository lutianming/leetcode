class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        n = len(num)
        if n <= 1:
            return [num]

        permutations = []
        for i in range(n):
            tmp = num[:]
            v = tmp.pop(i)
            sub = self.permute(tmp)
            for s in sub:
                s.append(v)
                permutations.append(s)
        return permutations
