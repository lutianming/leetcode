# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0

        if root.left and root.right:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            depth = min([left+1, right+1])
        elif root.left:
            depth = self.minDepth(root.left) + 1
        elif root.right:
            depth = self.minDepth(root.right) + 1
        else:
            depth = 1
        return depth
