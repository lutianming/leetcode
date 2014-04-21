# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        start = root
        curr = root
        next_start = None
        while start:
            if curr.left:
                if not next_start:
                    next_start = curr.left

                node, child = self.next_node(curr)
                if curr.right:
                    curr.left.next = curr.right
                    curr.right.next = child
                else:
                    curr.left.next = child
                curr = node

            elif curr.right:
                if not next_start:
                    next_start = curr.right
                node, child = self.next_node(curr)
                curr.right.next = child
                curr = node
            else:
                curr, _ = self.next_node(curr)

            if not curr:
                curr = next_start
                start = next_start
                next_start = None

    def next_node(self, node):
        node = node.next
        while node:
            if node.left:
                return node, node.left
            elif node.right:
                return node, node.right
            else:
                node = node.next
        return node, None
