class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return None

        op = 1
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif dividend < 0:
            op = -1
            dividend = -dividend
        elif divisor < 0:
            op = -1
            divisor = -divisor

        result = 0
        if divisor == 1:
            result = dividend
        else:
            while dividend > divisor:
                result += 1
                dividend -= divisor

        if op < 0:
            result = -result

        return result
