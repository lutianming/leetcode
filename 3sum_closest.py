class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSumClosest(self, num, target):
        sorted_num = sorted(num)
        distance = float('inf')
        sum = 0
        for i in range(len(num)-2):
            a = sorted_num[i]
            if a-target > distance:
                break
            if i > 0 and sorted_num[i-1] == a:
                continue
            j = i+1
            k = len(num)-1
            while(j < k):
                tmp = a + sorted_num[j] + sorted_num[k]
                d = tmp-target
                if abs(d) < distance:
                    distance = abs(d)
                    sum = tmp
                if d > 0:
                    k = k - 1
                    while(k >= 0 and sorted_num[k] == sorted_num[k+1]):
                        k = k - 1
                elif d < 0:
                    j = j+1
                    while(j < len(num) and sorted_num[j] == sorted_num[j-1]):
                        j = j + 1
                else:
                    return sum

        return sum

nums = [-13,10,11,-3,8,11,-4,8,12,-13,5,-6,-4,-2,12,11,7,-7,-3,10,
        12,13,-3,-2,6,-1,14,7,-13,8,14,-10,-4,10,-6,11,-2,-3,4,-13,
        0,-14,-3,3,-9,-6,-9,13,-6,3,1,-9,-6,13,-4,-15,-11,-12,7,-9,
        3,-2,-12,6,-15,-10,2,-2,-6,13,1,9,14,5,-11,-10,14,-5,11,-6,6,
        -3,-8,-15,-13,-4,7,13,-1,-9,11,-13,-4,-15,9,-4,12,-4,1,-9,-5,
        9,8,-14,-1,4,14]
nums1 = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

num2 = [1, 1, 1, 1]
solution = Solution()

print(solution.threeSumClosest(num2, 0))
