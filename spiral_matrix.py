class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        else:
            n = 0
        spiral = []
        left = 0
        right = n-1
        up = 0
        down = m-1
        direction = 'right'

        px = 0
        py = 0
        up = 1
        for i in range(m*n):
            spiral.append(matrix[px][py])
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
        return spiral

m = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s = Solution()
print(s.spiralOrder(m))
