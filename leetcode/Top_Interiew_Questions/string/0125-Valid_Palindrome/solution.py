import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(
            char.lower() for char in s if char.isalpha() or char.isdigit()
        )

        left, right = 0, len(cleaned_s) - 1

        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False

            left += 1
            right -= 1

        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub("[^a-zA-Z0-9]", "", s).lower()

        return cleaned_s == cleaned_s[::-1]
