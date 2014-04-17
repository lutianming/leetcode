# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast = head
        slow = head
        cycled = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycled = True
                break
        if not cycled:
            return None

        length = 0
        while True:
            slow = slow.next
            length += 1
            if slow == fast:
                break

        fast = head
        slow = head

        for i in range(length):
            fast = fast.next

        while True:
            if fast == slow:
                return fast

            fast = fast.next
            slow = slow.next
