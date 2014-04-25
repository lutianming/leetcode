from leetcode import ListNode


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k <= 0:
            return head

        num = 0
        node = head
        while node:
            node = node.next
            num += 1
        k = k % num
        if k == 0:
            return head

        fast = head
        for i in range(k):
            fast = fast.next
        slow = head

        while fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head
        head = slow.next
        slow.next = None
        return head

node = ListNode.from_list([1])
s = Solution()
print(s.rotateRight(node, 1))
