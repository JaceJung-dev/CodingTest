from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        if len(s) != len(t):
            return False

        for char in s:
            seen[char] = seen.get(char, 0) + 1

        for char in t:
            if char not in seen or seen[char] == 0:
                return False
            seen[char] -= 1

        return True


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            idx = ord(char) - ord("a")
            count[idx] += 1

        for char in t:
            idx = ord(char) - ord("a")
            if count[idx] == 0:
                return False
            count[idx] -= 1

        return True


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        return s_count == t_count


class Solution4:
    def isAnagram(self, s: str, t: str):
        s_count = Counter(s)
        t_count = Counter(t)

        return s_count == t_count
