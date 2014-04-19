class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        rows = []
        for i in range(numRows):
            n = i+1
            row = [1]*n
            for j in range(1, n-1):
                row[j] = rows[i-1][j-1] + rows[i-1][j]
            rows.append(row)
        return rows
