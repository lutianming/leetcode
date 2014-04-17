# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return None
        sorted = True
        node = head
        while node:
            next = node.next
            if next and next.val < node.val:
                sorted = False
                break
            node = node.next
        if sorted:
            return head

        sorted_head = head
        head = head.next
        sorted_head.next = None
        while head:
            next = head.next
            head.next = None
            prev = None
            node = sorted_head
            while node:
                if head.val < node.val:
                    tmp = head
                    tmp.next = node
                    if prev:
                        prev.next = tmp
                    else:
                        sorted_head = tmp
                    break
                else:
                    prev = node
                    node = node.next
            if not node:
                prev.next = head
            head = next
        return sorted_head

head = ListNode(3)
head.next = ListNode(4)
node = head.next
node.next = ListNode(1)

solution = Solution()
head = solution.insertionSortList(head)
while head:
    print(head.val)
    head = head.next
