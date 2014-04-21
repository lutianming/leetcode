class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path = [[0]*n for i in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 0:
                    if i > 0 and j > 0:
                        path[i][j] = path[i-1][j] + path[i][j-1]
                    elif i > 0:
                        path[i][j] = path[i-1][j]
                    elif j > 0:
                        path[i][j] = path[i][j-1]
                    else:
                        path[i][j] = 1
                else:
                    path[i][j] = 0
        return path[m-1][n-1]
