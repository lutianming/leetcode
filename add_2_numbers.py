# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = None
        node = None
        bit = 0
        while l1 and l2:
            s = l1.val + l2.val + bit

            if s >= 10:
                s = s-10
                bit = 1
            else:
                bit = 0

            if not head:
                head = ListNode(s)
                node = head
            else:
                node.next = ListNode(s)
                node = node.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val + bit
            if s >= 10:
                s = s-10
                bit = 1
            else:
                bit = 0
            node.next = ListNode(s)
            node = node.next
            l1 = l1.next

        while l2:
            s = l2.val + bit
            if s >= 10:
                s = s-10
                bit = 1
            else:
                bit = 0
            node.next = ListNode(s)
            node = node.next
            l2 = l2.next

        if bit:
            node.next = ListNode(bit)
        return head
