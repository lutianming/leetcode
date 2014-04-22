class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        result, _, _ = self.isValid(root)
        return result

    def isValid(self, root):
        if not root:
            return True, None, None

        result = True
        low = root.val
        high = root.val
        if root.left:
            left, llow, lhigh = self.isValid(root.left)
            if left and lhigh < root.val:
                low = llow
            else:
                return False, None, None

        if root.right:
            right, rlow, rhigh = self.isValid(root.right)
            if right and rlow > root.val:
                high = rhigh
            else:
                return False, None, None
        return result, low, high
