from leetcode import TreeNode


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        m = len(inorder)
        n = len(postorder)
        if m != n:
            return None
        if m == 0:
            return None

        val = postorder[-1]
        for i, v in enumerate(inorder):
            if v == val:
                break
        head = TreeNode(val)
        head.left = self.buildTree(inorder[0:i], postorder[0:i])
        head.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return head

s = Solution()
print(s.buildTree([2,1,4,3,5], [2,4,5,3,1]))
