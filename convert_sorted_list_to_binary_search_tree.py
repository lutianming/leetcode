# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from leetcode import TreeNode, ListNode

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            node = TreeNode(head.val)
            return node

        fast = head
        slow = head
        prev = None
        while fast.next and fast.next.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        node = TreeNode(slow.val)
        right = slow.next
        if prev:
            prev.next = None
            node.left = self.sortedListToBST(head)
        else:
            node.left = self.sortedListToBST(None)
        node.right = self.sortedListToBST(right)
        return node

a = [1,2,3,4]
l = ListNode.from_list(a)
s = Solution()
print(s.sortedListToBST(l))
