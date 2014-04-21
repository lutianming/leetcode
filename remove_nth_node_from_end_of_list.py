# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head

        last = head
        prev = None
        for i in range(n):
            if last:
                last = last.next
            else:
                if i == n-1:
                    i -= 1
                break
        if i < n-1:
            return head

        node = head
        while last:
            last = last.next
            prev = node
            node = node.next
        if prev:
            prev.next = node.next
        else:
            head = node.next
        return head

head = ListNode(1)
node = head
node.next = ListNode(2)
node = node.next
node.next = ListNode(3)
s = Solution()
head = s.removeNthFromEnd(head, 4)
print('=======')
while head:
    print(head.val)
    head = head.next
