class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if isinstance(board[0],list):
            board = [l[0] for l in board]
        x = len(board)
        y = len(board[0])
        for i in range(x):
            for j in range(y):
                pos = []
                if self._exist(board, pos, word, i, j, x, y):
                    return True
        return False

    def _exist(self, board, pos, word, i, j, x, y):
        if (i, j) in pos:
            return False

        if len(word) == 0:
            return True

        if i < 0 or i >= x or j < 0 or j >= y:
            return False

        if word[0] == board[i][j]:
            pos.append((i, j))

            if self._exist(board, pos, word[1:], i-1, j, x, y):
                return True

            if self._exist(board, pos, word[1:], i+1, j, x, y):
                return True

            if self._exist(board, pos, word[1:], i, j-1, x, y):
                return True

            if self._exist(board, pos, word[1:], i, j+1, x, y):
                return True
            pos.pop()
            return False

s = Solution()
# b = [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
# print(s.exist(b, "ABCCED"))
# print(s.exist(b, "SEE"))
# print(s.exist(b, "ABCD"))

b = ["aa"]
print(s.exist(b, 'aa'))
