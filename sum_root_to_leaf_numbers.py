# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0

        queue = []
        values = []
        self.dfs(root, queue, values)
        return sum(values)

    def dfs(self, root, queue, values):
        queue.append(root)
        if not root.left and not root.right:
            val = 0
            n = len(queue)
            for i in range(n):
                node = queue[n-i-1]
                val += node.val*10**i
            values.append(val)
        else:
            if root.left:
                self.dfs(root.left, queue, values)

            if root.right:
                self.dfs(root.right, queue, values)
        queue.pop()
