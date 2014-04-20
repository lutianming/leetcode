# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        n = len(num)
        if n == 0:
            return None

        middle = n/2
        head = TreeNode(num[middle])
        head.left = self.sortedArrayToBST(num[0:middle])
        head.right = self.sortedArrayToBST(num[middle+1:n])
        return head
