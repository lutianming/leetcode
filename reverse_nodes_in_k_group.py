from leetcode import ListNode


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head or not head.next or k==1:
            return head

        newhead = None
        head = head
        tail = head
        prev = None
        while True:
            count = 1
            while tail and tail.next and count < k:
                count += 1
                tail = tail.next
            if count != k:
                break

            node = head
            next = node.next
            for i in range(k-1):
                tmp = next.next
                next.next = node
                node = next
                next = tmp

            if not prev:
                newhead = tail
            else:
                prev.next = tail
            prev = head
            head.next = tmp
            head = tmp
            tail = head

        if not newhead:
            newhead = head
        return newhead

a = ListNode.from_list([1,2,3,4,5,6])
s = Solution()
print(s.reverseKGroup(a, 2))
