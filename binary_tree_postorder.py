# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        queue = []
        vals = []
        if not root:
            return vals

        queue.append(root)
        while len(queue) > 0:
            node = queue.pop()
            self.traversal(node, queue, vals)
        vals.reverse()
        return vals

    def traversal(self, root, queue, vals):
        vals.append(root.val)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
