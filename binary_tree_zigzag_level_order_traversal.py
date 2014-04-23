from leetcode import TreeNode


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        levels = []
        if not root:
            return levels
        stack = [root]
        direction = 1
        while stack:
            level = []
            next_stack = []
            while stack:
                node = stack.pop()
                level.append(node.val)
                if direction == 1:
                    first = node.left
                    next = node.right
                else:
                    first = node.right
                    next = node.left
                if first:
                    next_stack.append(first)
                if next:
                    next_stack.append(next)
            direction ^= 1

            levels.append(level)
            stack = next_stack
        return levels

a = [3,9,20,'#','#',15,7]
a = [1,2,3,4, '#', '#', 5]
tree = TreeNode.from_list(a)
s = Solution()
print(s.zigzagLevelOrder(tree))
