class Solution:
    # @return an integer
    def maxArea(self, height):
        maxarea = 0
        n = len(height)
        if n == 0:
            return maxarea

        i = 0
        j = n-1
        while i < j:
            left = height[i]
            right = height[j]
            area = (j-i)*min(left, right)
            if area > maxarea:
                maxarea = area
            if left < right:
                i += 1
            else:
                j -= 1
        return maxarea
