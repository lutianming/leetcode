class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        path = [[1]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i-1][j] + path[i][j-1]
        return path[m-1][n-1]
