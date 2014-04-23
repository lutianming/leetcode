from leetcode import ListNode


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        nodes = [node for node in lists if node]
        head = None
        curr = None
        while nodes:
            n = len(nodes)
            minv = float('inf')
            index = 0
            for i in range(n):
                node = nodes[i]
                if node.val < minv:
                    minv = node.val
                    index = i

            if not head:
                head = ListNode(minv)
                curr = head
            else:
                curr.next = ListNode(minv)
                curr = curr.next

            node = nodes[index].next
            if not node:
                nodes.pop(index)
            else:
                nodes[index] = node
        return head

a = ListNode.from_list([1,2,3])
b = ListNode.from_list([2,3,4])
s = Solution()
print(s.mergeKLists([a,b]))
