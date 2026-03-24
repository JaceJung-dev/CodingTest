class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for i, char in enumerate(s):
            if count[char] == 1:
                return i

        return -1


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        frequency = [0] * 26

        for char in s:
            idx = ord(char) - ord("a")
            frequency[idx] += 1

        for i, char in enumerate(s):
            idx = ord(char) - ord("a")
            if frequency[idx] == 1:
                return i

        return -1
