# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        vals = []
        if not root:
            return vals
        cache = [root]
        while len(cache) > 0:
            tmp = []
            level = []
            for node in cache:
                level.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            vals.append(level)
            cache = tmp
        vals.reverse()
        return vals
