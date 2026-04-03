class Solution:
    def reverse(self, x: int) -> int:

        result = 0
        if x < 0:
            x *= -1
            result = int(str(x)[::-1]) * -1
        else:
            result = int(str(x)[::-1])

        if result > 2**31 - 1 or result < -(2**31):
            return 0

        return result


class Solution2:
    def reverse(self, x: int) -> int:

        is_negative = False
        result = 0

        if x < 0:
            is_negative = True
            x *= -1

        while x > 0:
            result = result * 10 + x % 10
            x //= 10

        result = result * -1 if is_negative else result

        if result > 2**31 - 1 or result < -(2**31):
            return 0

        return result
