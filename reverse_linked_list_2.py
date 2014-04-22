# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode import ListNode

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        prev = None
        node = head
        i = 1
        while node and i < m:
            prev = node
            node = node.next
            i += 1

        tail = node
        next = node.next
        for i in range(n-m):
            tmp = next.next
            next.next = node
            node = next
            next = tmp
        if prev:
            prev.next = node
        else:
            head = node
        tail.next = next
        return head

node = ListNode.from_list([1,2,3,4,5])
s = Solution()
print(s.reverseBetween(node, 2, 5))
