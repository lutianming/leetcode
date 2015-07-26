class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        a = self.line(A, C, E, G)
        b = self.line(B, D, F, H)
        overlap = a*b
        return (C-A)*(D-B) + (G-E)*(H-F) - overlap

    def line(self, x1, x2, y1, y2):
        if y2 >= x2:
            if y1 >= x2:
                return 0
            elif y1 >= x1:
                return x2 - y1
            else:
                return x2-x1
        elif y2 >= x1:
            if y1 >= x1:
                return y2-y1
            else:
                return y2-x1
        else:
            return 0

s = Solution()
print(s.computeArea(0,0,0,0,-1,-1,1,1))
