class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num)
        if n <= 1:
            return num

        index = -1
        for i in range(1, n):
            if num[i] > num[i-1]:
                index = i

        if index == -1:
            return sorted(num)

        minv = num[index]
        j = index
        for i in range(index, n):
            if num[i] > num[index-1] and num[i] < minv:
                minv = num[i]
                j = i

        p = num[:]
        p[index-1], p[j] = p[j], p[index-1]
        p = p[:index] + sorted(p[index:])
        return p

a = [1,2,3]
# a = [3,2,1]
# a = [1,5,1]
# a = [1,3,2]
s = Solution()
print(s.nextPermutation(a))
