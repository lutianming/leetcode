class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        row = []
        for i in range(rowIndex+1):
            n = i+1
            tmp = [1]*n
            for j in range(1, n-1):
                tmp[j] = row[j-1] + row[j]
            row = tmp
        return row
