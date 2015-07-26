
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        left = 0
        right = n-1
        index = -1
        while left <= right:
            middle = left + (right-left)/2
            v = A[middle]
            if target == v:
                index = middle
                break
            elif left == right:
                    break

            if A[left] < A[right]:
                if target < v:
                    right = middle-1
                else:
                    left = middle+1
            else:
                if v >= A[left]:
                    if target < v and target >= A[left]:
                        right = middle-1
                    else:
                        left = middle+1
                else:
                    if target > v and target <= A[right]:
                        left = middle+1
                    else:
                        right = middle-1
        return index

a = [3, 4, 5, 6, 7, 0, 1, 2]
a = [3, 1]
s = Solution()
print(s.search(a, 1))
