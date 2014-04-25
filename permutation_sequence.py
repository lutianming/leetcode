class Solution:
    # @return a string
    def getPermutation(self, n, k):
        num = 1
        for i in range(n):
            num *= (i+1)
        if k < 1 or k > num:
            return None
        k = k-1
        seq = [i+1 for i in range(n)]
        permutation = ''
        subk = 1
        for i in range(n, 0, -1):
            for j in range(1, i):
                subk *= j
            index = k / subk
            k = k % subk
            subk = 1
            permutation += str(seq.pop(index))
        return permutation

s = Solution()
print(s.getPermutation(1, 1))
