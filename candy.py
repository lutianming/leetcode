class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)
        if n == 1:
            return 1
        count = 1
        length = 0
        state = 0
        high = 0

        def addCount(count, high):
            if state > 0:
                count += (2+length+1)*length/2
                high = length+1
            elif state < 0:
                count += (1+length)*length/2
                if high > 0 and (length+1) > high:
                    count += length+1-high
                high = 1
            else:
                count += length
                high = 1
            return count, high

        for i, v in enumerate(ratings):
            if i == 0:
                continue
            if v > ratings[i-1]:
                if state > 0:
                    length += 1
                else:
                    count, high = addCount(count, high)
                    length = 1
            elif v < ratings[i-1]:
                if state < 0:
                    length += 1
                else:
                    count, high = addCount(count, high)
                    length = 1
            else:
                if state == 0:
                    length += 1
                else:
                    count, high = addCount(count, high)
                    length = 1
            state = v-ratings[i-1]

        count, high = addCount(count, high)
        return count

ratings = [1,2,2, 2, 1, 0, -1]
ratings = [1, 0, 2]
ratings = [2, 3, 2]
solution = Solution()
print(solution.candy(ratings))
