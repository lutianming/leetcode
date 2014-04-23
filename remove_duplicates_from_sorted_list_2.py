from leetcode import ListNode


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        prev = None
        newhead = None
        node = head
        dup = None
        while node:
            if node.next and node.val == node.next.val:
                dup = node.val
                node.next = node.next.next
            elif node.val == dup:
                if prev:
                    prev.next = node.next
                dup = None
                node = node.next
            else:
                if not newhead:
                    newhead = node
                prev = node
                node = node.next
        return newhead

a = [1,2,3,3,4,4,5]
a = [1,1, 2, 2]
head = ListNode.from_list(a)
s = Solution()
print(s.deleteDuplicates(head))
