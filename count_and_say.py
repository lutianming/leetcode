class Solution:
    # @return a string
    def countAndSay(self, n):
        say = '1'
        for i in range(n-1):
            say = self._count_say(say)
        return say

    def _count_say(self, s):
        curr = None
        count = 0
        say = ""
        for c in s:
            if c == curr:
                count += 1
            else:
                if curr:
                    say += str(count)+str(curr)
                curr = c
                count = 1
        say += str(count)+str(curr)
        return say

s = Solution()
print(s.countAndSay(4))
