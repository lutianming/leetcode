from leetcode import TreeNode


class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        m = len(preorder)
        n = len(inorder)
        if m != n:
            return None
        if m == 0:
            return None

        val = preorder[0]
        for i, v in enumerate(inorder):
            if v == val:
                break
        head = TreeNode(val)
        head.left = self.buildTree(preorder[1:i+1], inorder[0:i])
        head.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return head

s = Solution()
print(s.buildTree([1,2,3,4,5], [2,1,4,3,5]))
