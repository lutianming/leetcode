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
        link = {i: list() for i in range(n)}

        for i in range(n, 0, -1):
            index = i-1
            for j in range(index, n):
                sub = s[index:j+1]
                if sub in dict and pivot[j+1]:
                    pivot[index] = True
                    link[index].append(j+1)

        words = []
        sentences = []

        def traversal(i):
            if i == n:
                sentences.append(" ".join(words))
                return

            indices = link[i]
            for j in indices:
                word = s[i:j]
                words.append(word)
                traversal(j)
                words.pop()
        traversal(0)
        return sentences

s = "catsanddog"
d = ["cat", "cats", "and", "sand", "dog"]
s = 'a'
d = []
solution = Solution()
print(solution.wordBreak(s, d))
