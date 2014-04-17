class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        single_bits = []
        for i in range(32):
            bits = [(a >> i) & 1 for a in A]
            bit = sum(bits) % 3
            single_bits.append(bit)
        single = 0
        for i, bit in enumerate(single_bits):
            if i == 31:
                single -= bit*2**i
            else:
                single += bit*2**i
        return single

A = [1,1,1,2,2,2,3]
A = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
solution = Solution()
print(solution.singleNumber(A))
