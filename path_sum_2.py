# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        paths = []
        stack = []
        self.dfs(root, sum, stack, paths)
        return paths

    def dfs(self, node, sum, stack, paths):
        stack.append(node)
        if not node:
            stack.pop()
            return

        if not node.left and not node.right:
            if node.val == sum:
                path = [p.val for p in stack]
                paths.append(path)
        else:
            if node.left:
                self.dfs(node.left, sum-node.val, stack, paths)
            if node.right:
                self.dfs(node.right, sum-node.val, stack, paths)
        stack.pop()
