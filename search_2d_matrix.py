class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        result = False
        x = len(matrix)
        if x == 0:
            return result
        y = len(matrix[0])
        for i in range(x):
            left = matrix[i][0]
            right = matrix[i][y-1]
            if target >= left and target <= right:
                for j in range(y):
                    if target == matrix[i][j]:
                        result = True
                        break
                break
        return result
