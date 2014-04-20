# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        result = True
        if not root:
            return result
        cache = [root.left, root.right]

        while len(cache) > 0:
            n = len(cache)
            tmp = []
            for i in range(0, n, 2):
                left = cache[i]
                right = cache[i+1]
                if left and right:
                    if left.val != right.val:
                        result = False
                        break
                    else:
                        tmp.append(left.left)
                        tmp.append(right.right)
                        tmp.append(left.right)
                        tmp.append(right.left)
                elif not left and not right:
                    pass
                else:
                    result = False
                    break
            cache = tmp
        return result

node = TreeNode(1)
node.right = TreeNode(2)
s = Solution()
print(s.isSymmetric(node))
