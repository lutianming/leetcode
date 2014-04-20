class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for gap in range(0, n/2):
            for i in range(0, n-2*gap-1):
                prev = matrix[gap][gap+i]

                x = gap+i
                y = n-1-gap
                tmp = matrix[x][y]
                matrix[x][y] = prev
                prev = tmp

                x = n-1-gap
                y = n-1-gap-i
                tmp = matrix[x][y]
                matrix[x][y] = prev
                prev = tmp

                x = n-1-gap-i
                y = gap
                tmp = matrix[x][y]
                matrix[x][y] = prev
                prev = tmp

                x = gap
                y = gap+i
                matrix[x][y] = prev

        return matrix

m = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
m = [[1,2],
     [4,3]]
print('======')
for row in m:
    print(row)
s = Solution()
s.rotate(m)
print('======')
for row in m:
    print(row)
