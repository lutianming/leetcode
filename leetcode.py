class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        curr = self
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return str(vals)

    @classmethod
    def from_list(cls, vals):
        head = None
        curr = None
        for i in vals:
            node = ListNode(i)
            if not head:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node
        return head


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        queue = [self]
        s = ''
        while len(queue) > 0:
            next_queue = []
            for node in queue:
                s += node.val.__str__() + '\t'
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            s += '\n'
            queue = next_queue
        return s

    @classmethod
    def from_list(cls, vals):
        n = len(vals)
        if n == 0:
            return None
        head = TreeNode(vals[0])

        level = [head]

        i = 1
        while i < n:
            next_level = []
            for node in level:
                v = vals[i]
                if v != '#':
                    left = TreeNode(v)
                    node.left = left
                    next_level.append(left)

                i += 1
                if i >= n:
                    break
                v = vals[i]
                if v != '#':
                    right = TreeNode(v)
                    node.right = right
                    next_level.append(right)
                i += 1
                if i >= n:
                    break
            level = next_level
        return head
