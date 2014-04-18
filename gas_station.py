class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        i = 0
        while i < n:
            gasleft = 0
            for j in range(i, n+i):
                index = j % n
                gasleft += gas[index] - cost[index]
                if gasleft < 0:
                    break
            if gasleft >= 0:
                return i
            if i == j:
                i += 1
            else:
                i = j

        return -1

gas = [4]
cost = [5]
