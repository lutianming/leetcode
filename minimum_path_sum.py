class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        path = [[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    p1 = path[i-1][j]
                    p2 = path[i][j-1]
                    p = min(p1, p2)
                elif i > 0:
                    p = path[i-1][j]
                elif j > 0:
                    p = path[i][j-1]
                else:
                    p = 0
                path[i][j] = p + grid[i][j]
        return path[m-1][n-1]

grid = [[1,2],[1,1]]
s = Solution()
print(s.minPathSum(grid))
