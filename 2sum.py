class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        sorted_num = sorted(num)
        n = len(num)
        i = 0
        j = n-1
        while(i < j):
            a = sorted_num[i]
            b = sorted_num[j]
            tmp = a + b
            if tmp > target:
                j -= 1
            elif tmp < target:
                i += 1
            else:
                index1 = num.index(a)+1
                rnum = num[::-1]
                index2 = n-rnum.index(b)
                return sorted([index1, index2])


S = [2, 7, 11, 15]
solution = Solution()
print(solution.twoSum(S, 9))
