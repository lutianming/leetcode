# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q

        if p.val != q.val:
            is_same = False
        else:
            is_same_left = self.isSameTree(p.left, q.left)
            is_same_right = self.isSameTree(p.right, q.right)
            is_same = is_same_left and is_same_right
        return is_same
