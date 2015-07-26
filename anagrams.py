class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        groups = {}
        for s in strs:
            counts = [0]*26
            for c in s:
                index = ord(c) - ord('a')
                counts[index] += 1
            key = tuple(counts)
            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        group = [item for group in groups.values() if len(group)>1 for item in group]
        return group

s = Solution()
print(s.anagrams(['']))
