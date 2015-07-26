# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        count_a = 0
        count_b = 0
        node = headA
        while node:
            count_a += 1
            node = node.next

        node = headB
        while node:
            count_b += 1
            node = node.next

        h_a = headA
        h_b = headB
        if count_a < count_b:
            for i in range(count_b - count_a):
                h_b = h_b.next
        elif count_b < count_a:
            for i in range(count_a - count_b):
                h_a = h_a.next

        while h_a:
            if h_a == h_b:
                return h_a
            h_a = h_a.next
            h_b = h_b.next
        return None
