class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        k = len(s3)
        if k != (m+n):
            return False
        matrix = [[0]*(n+1) for i in range(m+1)]
        return self._interleave(s1, 0, s2, 0, s3, 0, matrix) == 1

    def _interleave(self, s1, i, s2, j, s3, k, matrix):
        if i == len(s1):
            if s2[j:] == s3[k:]:
                return 1
            else:
                return -1
        if j == len(s2):
            if s1[i:] == s3[k:]:
                return 1
            else:
                return -1

        if matrix[i][j] != 0:
            return matrix[i][j]

        case1 = self._interleave(s1, i+1, s2, j, s3, k+1, matrix)
        case1 = s1[i] == s3[k] and case1 == 1
        case2 = self._interleave(s1, i, s2, j+1, s3, k+1, matrix)
        case2 = s2[j] == s3[k] and case2 == 1
        if case1 or case2:
            matrix[i][j] = 1
        else:
            matrix[i][j] = -1
        return matrix[i][j]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
#s3 = "aadbbbaccc"
# s1 = "bacbacbabacbab"
# s2 = "bbbcaacaacba"
# s3 = "bbabcbbacacabcbacbaaaabbac"
s = Solution()
print(s.isInterleave(s1, s2, s3))
