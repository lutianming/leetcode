# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        nodes = {}
        newHead = RandomListNode(head.label)
        newNode = newHead
        nodes[head] = newHead
        node = head.next
        while node:
            n = RandomListNode(node.label)
            newNode.next = n
            newNode = n

            nodes[node] = n
            node = node.next

        node = head
        while node:
            newNode = nodes[node]
            if node.random:
                newNode.random = nodes[node.random]
            else:
                newNode.random = None
            node = node.next

        return newHead
