class Solution:
# @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0]*n for i in range(n)]
        left = 0
        right = n-1
        up = 0
        down = n-1
        direction = 'right'

        px = 0
        py = 0
        up = 1
        for i in range(1, n*n+1):
            matrix[px][py] = i
            if direction == 'right':
                if py == right:
                    direction = 'down'
                    right -= 1
                    px += 1
                else:
                    py += 1
            elif direction == 'down':
                if px == down:
                    direction = 'left'
                    down -= 1
                    py -= 1
                else:
                    px += 1
            elif direction == 'left':
                if py == left:
                    direction = 'up'
                    left += 1
                    px -= 1
                else:
                    py -= 1
            elif direction == 'up':
                if px == up:
                    direction = 'right'
                    up += 1
                    py += 1
                else:
                    px -= 1
        return matrix

s = Solution()
print(s.spiralOrder(3))
