class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        m = len(S)
        n = len(T)
        matrix = [[0]*(m+1) for i in range(n+1)]
        for i in range(m+1):
            matrix[0][i] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                sub = matrix[i-1][j-1] if S[j-1] == T[i-1] else 0
                matrix[i][j] = matrix[i][j-1]+sub
        return matrix[n][m]

S = "rabbbit"
T = "rabbit"
S = 'ccc'
T = 'c'
s = Solution()
print(s.numDistinct(S, T))
