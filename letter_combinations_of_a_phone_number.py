class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        digitmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        combines = [""]
        for d in digits:
            tmp = []
            for c in digitmap[d]:
                for s in combines:
                    tmp.append(s+c)
            combines = tmp
        return combines

a = '23'
s = Solution()
print(s.letterCombinations(a))
