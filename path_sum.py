# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False

        sub = sum-root.val == 0
        if root.left:
            left = self.hasPathSum(root.left, sum-root.val)
        else:
            left = sub

        if root.right:
            right = self.hasPathSum(root.right, sum-root.val)
        else:
            right = sub

        if root.left and root.right:
            result = right or left
        elif root.left:
            result = left
        elif root.right:
            result = right
        else:
            result = sub
        return result
