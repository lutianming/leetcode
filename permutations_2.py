class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num = sorted(num)
        return self.permute(num)

    def permute(self, num):
        n = len(num)
        if n <= 1:
            return [num]

        permutations = []
        curr = None
        for i in range(n):
            tmp = num[:]
            if tmp[i] == curr:
                continue
            curr = tmp.pop(i)
            sub = self.permute(tmp)
            for s in sub:
                s.append(curr)
                permutations.append(s)
        return permutations

a = [3,3,1,2,3,2,3,1]
a = [1,1,2]
# a = [1,1,0,0,1,-1,-1,1]
s = Solution()
print(s.permuteUnique(a))
