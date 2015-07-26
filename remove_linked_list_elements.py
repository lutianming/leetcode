# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        node = head
        last = None
        new_head = head
        while node:
            if node.val != val:
                if last:
                    last.next = node
                    last = node
                else:
                    last = node
                    new_head = node
            node = node.next
        if last:
            last.next = None
        else:
            new_head = None
        return new_head
