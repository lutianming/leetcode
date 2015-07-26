class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')

        max_len = max(len(v1), len(v2))
        if len(v1) < max_len:
            a = ['0'] * (max_len - len(v1))
            v1 = v1 + a
        if len(v2) < max_len:
            a = ['0'] * (max_len - len(v2))
            v2 = v2 + a
        for n1, n2 in zip(v1, v2):
            n1 = int(n1)
            n2 = int(n2)
            if n1 < n2:
                return -1
            if n1 > n2:
                return 1
        return 0

s = Solution()
print(s.compareVersion('1', '1.0'))
