# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        lowhead = None
        lowtail = None
        highhead = None
        hightail = None
        curr = head
        while curr:
            if curr.val < x:
                if lowtail:
                    lowtail.next = curr
                    lowtail = curr
                else:
                    lowhead = curr
                    lowtail = curr
            else:
                if hightail:
                    hightail.next = curr
                    hightail = curr
                else:
                    highhead = curr
                    hightail = curr
            curr = curr.next
        if lowtail:
            lowtail.next = highhead
        else:
            lowhead = highhead
        if hightail:
            hightail.next = None
        return lowhead
