# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
        _, result = self.balanced(root)
        return result

    def balanced(self, root):
        if not root:
            return 0, True
        dleft, left = self.balanced(root.left)
        dright, right = self.balanced(root.right)
        depth = max(dleft+1, dright+1)
        return (depth, left and right and abs(dleft-dright) <= 1)
