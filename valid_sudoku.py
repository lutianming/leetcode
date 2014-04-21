class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        bits = [0]*9
        n = len(board)
        valid = True

        #rows
        for i in range(n):
            for j in range(n):
                v = board[i][j]
                if v != '.':
                    v = int(v)
                    if bits[v-1] == 1:
                        valid = False
                        break
                    else:
                        bits[v-1] = 1
            if not valid:
                break
            bits = [0]*9
        if not valid:
            return valid

        #cols
        for i in range(n):
            for j in range(n):
                v = board[j][i]
                if v != '.':
                    v = int(v)
                    if bits[v-1] == 1:
                        valid = False
                        break
                    else:
                        bits[v-1] = 1
            if not valid:
                break
            bits = [0]*9
        if not valid:
            return valid

        #small squares
        for i in range(n/3):
            for j in range(n/3):
                for a in range(3):
                    for b in range(3):
                        v = board[i*3+a][j*3+b]
                        if v != '.':
                            v = int(v)
                            if bits[v-1] == 1:
                                valid = False
                                break
                            else:
                                bits[v-1] = 1
                if not valid:
                    break
                bits = [0]*9
        return valid
