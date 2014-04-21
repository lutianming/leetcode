class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        path = [0]*(n+1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                v = row[i]
                path[i] = min(path[i]+v, path[i+1]+v)
        return path[0]
