# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printlist(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    print(l)

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        """
        time: O(nlog(n))
        space: 1
        """
        if not head or not head.next:
            return head
        k = 1
        sorted_head = head
        while True:
            print('k=', k)
            sorted_head, nmerge = self._merge(sorted_head, k)
            printlist(sorted_head)
            if nmerge == 1:
                break
            k *= 2
        return sorted_head

    def _merge(self, head, k):
        sorted_head = None
        sorted_node = None
        p = head
        q = head
        nmerge = 0
        while p:
            nmerge += 1
            psize = 0
            qsize = k
            for i in range(k):
                if q:
                    q = q.next
                    psize += 1
                else:
                    break
            pnode = p
            qnode = q

            while psize > 0 or (qsize > 0 and qnode):
                # print(psize, qsize)
                # printlist(pnode)
                # printlist(qnode)
                if not psize > 0:
                    node = qnode
                    qnode = qnode.next
                    qsize -= 1
                elif not (qsize > 0 and qnode):
                    node = pnode
                    pnode = pnode.next
                    psize -= 1

                elif pnode.val <= qnode.val:
                    node = pnode
                    pnode = pnode.next
                    psize -= 1
                else:
                    node = qnode
                    qnode = qnode.next
                    qsize -= 1

                if not sorted_head:
                    sorted_head = node
                    sorted_node = node
                else:
                    sorted_node.next = node
                    sorted_node = node
                    node.next = None
            p = qnode
            q = qnode
        return sorted_head, nmerge

vals = [1,2,3,-2,3,4,-4,-4,-5,-6,7,-7]
print(len(vals))
def buildList(vals):
    head = None
    node = None
    for val in vals:
        tmp = ListNode(val)
        if not head:
            head = tmp
            node = tmp
        else:
            node.next = tmp
            node = tmp
    return head
head = buildList(vals)
solution = Solution()
head = solution.sortList(head)
printlist(head)
