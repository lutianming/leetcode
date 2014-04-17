# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return head

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        lasthalf = slow.next
        lasthalf = self.reverse(lasthalf)
        slow.next = None

        firsthalf = head

        while lasthalf:
            a = firsthalf.next
            b = lasthalf.next
            firsthalf.next = lasthalf
            lasthalf.next = a
            firsthalf = a
            lasthalf = b
        return head

    def reverse(self, head):
        if not head:
            return head
        next = head.next
        head.next = None
        while next:
            tmp = next.next
            next.next = head
            head = next
            next = tmp
        return head

head = ListNode(1)
head.next = ListNode(2)
# node = head.next
# node.next = ListNode(3)
# node = node.next
# node.next = ListNode(4)
solution = Solution()
head = solution.reorderList(head)
while head:
    print(head.val)
    head = head.next
