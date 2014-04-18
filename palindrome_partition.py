class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        matrix = self.build_matrix(s)
        queue = []
        partitions = []
        self.dfs(matrix, s, 0, queue, partitions)
        return partitions

    def dfs(self, matrix, s, i, queue, partitions):
        n = len(s)
        if i == n:
            partitions.append(list(queue))
            return

        for j in range(i, n):
            if matrix[i][j]:
                queue.append(s[i:j+1])
                self.dfs(matrix, s, j+1, queue, partitions)
                queue.pop()

    def build_matrix(self, s):
        n = len(s)
        matrix = [[0]*n for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if self.is_palindrome(sub):
                    matrix[i][j] = 1
        return matrix

    def is_palindrome(self, s):
        n = len(s)
        if n == 0:
            return False
        i = 0
        j = n-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

s = "abab"
solution = Solution()
print(solution.partition(s))
