# 242. Valid Anagram

## 문제

- 링크: https://leetcode.com/problems/valid-anagram/
- 난이도: Easy
- 태그: Hash Table, String, Sorting

## 접근 방식

### Solution 1 — Hash Map (카운트 증감)

- s로 빈도수를 올리고, t로 차감
- 차감 시 없거나 0이면 False

### Solution 2 — 배열 카운팅

- 크기 26 배열로 Solution 1과 동일한 로직 수행

### Solution 3 — 두 Hash Map 비교

- s, t 각각의 빈도수 dict를 만들어 동치 비교

### Solution 4 — Counter 비교

- `Counter` 사용

## 풀이

### Solution 1

```python
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
```

### Solution 2

```python
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
```

### Solution 3

```python
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
```

### Solution 4

```python
from collections import Counter

class Solution4:
    def isAnagram(self, s: str, t: str):
        s_count = Counter(s)
        t_count = Counter(t)

        return s_count == t_count
```

## 복잡도

|            | 시간 | 공간                     |
| ---------- | ---- | ------------------------ |
| Solution 1 | O(n) | O(k) — k는 고유 문자 수  |
| Solution 2 | O(n) | O(1) — 고정 크기 26 배열 |
| Solution 3 | O(n) | O(k)                     |
| Solution 4 | O(n) | O(k)                     |

## 배운 점

- Solution 1·2는 하나의 카운터로 증감, Solution 3·4는 두 카운터를 비교
- `len(s) != len(t)` 조기 체크로 불필요한 연산을 줄일 수 있음
