# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        node = head
        while node:
            if not node.next:
                break
            next = node.next
            if next.val == node.val:
                node.next = next.next
            else:
                node = node.next
        return head
