# 28. Find the Index of the First Occurrence in a String

## 문제

- 링크: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
- 난이도: Easy
- 태그: Two Pointers, String, String Matching

## 접근 방식

### Solution 1 — 문자 단위 비교

- 외부 루프로 시작 위치를 잡고, 내부 루프로 needle과 한 글자씩 비교
- 불일치 시 break, 내부 루프를 끝까지 돌면(`for-else`) 매칭 성공

### Solution 2 — 슬라이싱 비교

- 각 위치에서 `haystack[i:i+m]`으로 needle 길이만큼 잘라서 동치 비교

## 풀이

### Solution 1

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i

        return -1
```

### Solution 2

```python
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        if n < m:
            return -1

        for i in range(n):
            if haystack[i : i + m] == needle:
                return i

        return -1
```

## 복잡도

|            | 시간      | 공간                              |
| ---------- | --------- | --------------------------------- |
| Solution 1 | O(n \* m) | O(1)                              |
| Solution 2 | O(n \* m) | O(m) — 슬라이싱 시 새 문자열 생성 |

## 배운 점

- 파이썬 `for-else` 문법: 루프가 break 없이 끝나면 else 블록 실행
- 슬라이싱은 간결하지만 매번 새 문자열을 만들어 공간 O(m) 소모
- 더 최적화된 문자열 매칭은 KMP(O(n+m)) 알고리즘이 있음
