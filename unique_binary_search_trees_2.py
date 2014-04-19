# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self._generate(n, 1)

    def _generate(self, n, base):
        nodes = []
        if n == 0:
            nodes.append(None)
            return nodes

        for i in range(n):
            val = base+i
            leftnodes = self._generate(i, base)
            rightnodes = self._generate(n-1-i, val+1)

            for left in leftnodes:
                for right in rightnodes:
                    node = TreeNode(val)
                    node.left = left
                    node.right = right
                    nodes.append(node)
        return nodes

n = 4
solution = Solution()
nodes = solution.generateTrees(n)
print(len(nodes))
