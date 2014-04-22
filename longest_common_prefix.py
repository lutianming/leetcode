class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ''
        if n == 1:
            return strs[0]

        prefix = ''
        m = min([len(s) for s in strs])
        for i in range(m):
            first = strs[0]
            common = True
            for s in strs[1:]:
                if first[i] != s[i]:
                    common = False
                    break
            if not common:
                break
            else:
                prefix += first[i]
        return prefix
