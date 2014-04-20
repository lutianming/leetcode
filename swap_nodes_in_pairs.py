# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        node = head
        prev = None
        while node and node.next:
            tmp = node.next
            node.next = tmp.next
            tmp.next = node
            node = node.next
            if prev:
                prev.next = tmp
            else:
                head = tmp
            prev = tmp.next
        return head
