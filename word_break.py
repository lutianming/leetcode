class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        """
        DP solution
        """
        n = len(s)
        pivot = [False]*(n+1)
        pivot[n] = True

        for i in range(n, 0, -1):
            index = i-1
            for j in range(index, n):
                sub = s[index:j+1]
                if sub in dict and pivot[j+1]:
                    pivot[index] = True
                    break
        return pivot[0]

s = "leetcode"
d = ["leet", "code"]
solution = Solution()
print(solution.wordBreak(s, d))
