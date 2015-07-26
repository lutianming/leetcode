class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = []
        items = path.split('/')
        for item in items:
            if len(item) == 0:
                continue

            if item == '.':
                continue
            elif item == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(item)

        return '/'+'/'.join(stack)

s = Solution()
print(s.simplifyPath('/../'))
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/a/./b/../../c/"))
