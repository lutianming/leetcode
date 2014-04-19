# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = None
        curr = None
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    node = ListNode(l1.val)
                    l1 = l1.next
                else:
                    node = ListNode(l2.val)
                    l2 = l2.next
            else:
                if l1:
                    node = ListNode(l1.val)
                    l1 = l1.next
                else:
                    node = ListNode(l2.val)
                    l2 = l2.next
            if not head:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node
        return head
