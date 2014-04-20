class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        queens = []
        configs = []
        row = 0
        col = 0
        while True:
            added = False
            for j in range(col, n):
                conflict = self.attack(row, j, queens)
                if not conflict:
                    queens.append(j)
                    added = True
                    break
            if added:
                if row == n-1:
                    configs.append(self.get_config(queens))
                    col = queens.pop() + 1
                else:
                    row += 1
                    col = 0
            else:
                if row == 0 and col >= n:
                    break
                row -= 1
                col = queens.pop() + 1

        return configs

    def attack(self, i, j, queens):
        result = False
        for i2, j2 in enumerate(queens):
            if i == i2:
                result = True
                break
            if j == j2:
                result = True
                break
            if abs(i-i2) == abs(j-j2):
                result = True
                break
        return result

    def get_config(self, queens):
        config = []
        n = len(queens)
        for j in queens:
            s = '.'*j
            s += 'Q'
            s += '.'*(n-1-j)
            config.append(s)
        return config

n = 4
s = Solution()
print(s.solveNQueens(n))
