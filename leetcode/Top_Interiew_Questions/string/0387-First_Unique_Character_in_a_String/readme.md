# 387. First Unique Character in a String

## 문제

- 링크: https://leetcode.com/problems/first-unique-character-in-a-string/
- 난이도: Easy
- 태그: Hash Table, String, Queue, Counting

## 접근 방식

### Solution 1 — Hash Map

- 1차 순회: dict로 각 문자의 등장 횟수 기록
- 2차 순회: count가 1인 첫 번째 문자의 인덱스 반환

### Solution 2 — 배열 카운팅

- 소문자만 존재하므로 크기 26 배열로 빈도수 기록
- `ord(char) - ord("a")`로 인덱스 변환

## 풀이

### Solution 1

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for i, char in enumerate(s):
            if count[char] == 1:
                return i

        return -1
```

### Solution 2

```python
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
```

## 복잡도

|            | 시간 | 공간                     |
| ---------- | ---- | ------------------------ |
| Solution 1 | O(n) | O(k) — k는 고유 문자 수  |
| Solution 2 | O(n) | O(1) — 고정 크기 26 배열 |

## 배운 점

- 두 풀이 모두 "빈도 세기 + 재순회" 패턴 — 같은 로직을 dict vs 배열로 표현
- 문자 종류가 제한적(소문자 26개)이면 배열이 공간적으로 O(1)이라 유리
