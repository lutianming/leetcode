class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        x = len(matrix)
        if x > 0:
            y = len(matrix[0])
        else:
            y = 0
        rows = [1]*x
        cols = [1]*y

        for i in range(x):
            for j in range(y):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0

        for i in range(x):
            if rows[i] == 0:
                for j in range(y):
                    matrix[i][j] = 0

        for j in range(y):
            if cols[j] == 0:
                for i in range(x):
                    matrix[i][j] = 0

m = [[1,1,1],[0,1,2]]
s = Solution()
s.setZeroes(m)
print(m)
