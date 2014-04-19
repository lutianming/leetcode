# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0

        if root.left and root.right:
            left = self.maxDepth(root.left) + 1
            right = self.maxDepth(root.right) + 1
            depth = max([left, right])
        elif root.left:
            depth = self.maxDepth(root.left) + 1
        elif root.right:
            depth = self.maxDepth(root.right) + 1
        else:
            depth = 1
        return depth
