class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        left = 0
        right = n-1
        result = False
        while left <= right:
            while left+1 < n:
                if A[left] == A[left+1]:
                    left += 1
                else:
                    break

            while right-1 >= left:
                if A[right] == A[right-1]:
                    right -= 1
                elif left != right and A[right] == A[left]:
                    right -= 1
                else:
                    break
            middle = left + (right-left)/2
            v = A[middle]
            if target == v:
                result = True
                break
            else:
                if left == right:
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
        return result

a = [3, 3, 3, 4, 5, 6, 7, 0, 1, 2]
a = [1, 3, 1, 1, 1]
a = [1, 1, 2, 2, 1]
s = Solution()
print(s.search(a, 2))
