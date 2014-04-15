# class Solution:
#     # @return a list of lists of length 4, [[val1,val2,val3,val4]]
#     #without hash, O(N^3)
#     def fourSum(self, num, target):
#         sorted_num = sorted(num)
#         n = len(num)
#         result = []
#         for i in range(n-3):
#             a = sorted_num[i]
#             if a > target:
#                 break
#             if i > 0 and sorted_num[i-1] == a:
#                 continue
#             for j in range(i+1, n-2):
#                 b = sorted_num[j]
#                 if a+b > target:
#                     break
#                 if j > i+1 and sorted_num[j-1] == b:
#                     continue
#                 k = j+1
#                 l = n-1
#                 while(k < l):
#                     c = sorted_num[k]
#                     d = sorted_num[l]
#                     tmp = a + b + c + d
#                     if tmp < target:
#                         k += 1
#                         while(k < n and sorted_num[k-1] == sorted_num[k]):
#                             k += 1
#                     elif tmp > target:
#                         l -= 1
#                         while(l > 0 and sorted_num[l+1] == sorted_num[l]):
#                             l -= 1
#                     else:
#                         result.append((a, b, c, d))
#                         k += 1
#                         while(k < n and sorted_num[k-1] == sorted_num[k]):
#                             k += 1
#                         l -= 1
#                         while(l > 0 and sorted_num[l+1] == sorted_num[l]):
#                             l -= 1
#         return result

from collections import defaultdict

class Solution:
    def fourSum(self, num, target):
        sorted_num = sorted(num)
        pairvalues = defaultdict(list)
        result = []
        for i, v1 in enumerate(sorted_num[:-1]):
            for j, v2 in enumerate(sorted_num[i+1:]):
                v = v1+v2
                pairvalues[v].append((i, j+i+1))
        keys = sorted(pairvalues.keys())
        n = len(keys)
        i = 0
        j = n-1
        while(i <= j):
            k1 = keys[i]
            k2 = keys[j]
            tmp = k1 + k2
            if tmp > target:
                j -= 1
            elif tmp < target:
                i += 1
            else:
                pairs1 = pairvalues[k1]
                pairs2 = pairvalues[k2]
                for p1 in pairs1:
                    for p2 in pairs2:
                        if p1[0] not in p2 and p1[1] not in p2:
                            a = sorted_num[p1[0]]
                            b = sorted_num[p1[1]]
                            c = sorted_num[p2[0]]
                            d = sorted_num[p2[1]]
                            t = sorted([a, b, c, d])
                            if t not in result:
                                result.append(t)
                i += 1
                j -= 1
        return result

S = [1, 0, -1, 0, -2, 2]
S = [0,0,0,0]
solution = Solution()
print(solution.fourSum(S, 0))
