class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


class Solution2:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)

        carry = 1
        for i in range(n - 1, -1, -1):
            tmp = digits[i] + carry
            digits[i] = tmp % 10
            carry = tmp // 10
        if carry:
            digits = [1] + digits

        return digits
