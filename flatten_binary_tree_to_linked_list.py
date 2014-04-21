# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        head, _ = self._flatten(root)
        return head

    def _flatten(self, root):
        if not root:
            return root, root

        head = root
        tail = root
        left = root.left
        right = root.right
        root.left = None
        root.right = None
        if left:
            left_head, left_tail = self._flatten(left)
            tail.right = left_head
            tail = left_tail
        if right:
            right_head, right_tail = self._flatten(right)
            tail.right = right_head
            tail = right_tail
        return head, tail
