# 125. Valid Palindrome

## 문제

- 링크: https://leetcode.com/problems/valid-palindrome/
- 난이도: Easy
- 태그: Two Pointers, String

## 접근 방식

### Solution 1 — 전처리 + Two Pointers

- 영문자/숫자만 남기고 소문자로 변환
- 양 끝에서 좁혀오는 투 포인터로 비교
- 참고: `char.isalpha() or char.isdigit()`는 `char.isalnum()`으로 대체 가능

### Solution 2 — 정규식 + 슬라이싱

- `re.sub`으로 영문자/숫자 외 제거 후 소문자 변환
- `[::-1]`로 뒤집어서 동치 비교

## 풀이

### Solution 1

```python
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
```

### Solution 2

```python
import re

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub("[^a-zA-Z0-9]", "", s).lower()

        return cleaned_s == cleaned_s[::-1]
```

## 복잡도

|            | 시간 | 공간                 |
| ---------- | ---- | -------------------- |
| Solution 1 | O(n) | O(n) — 정제된 문자열 |
| Solution 2 | O(n) | O(n) — 정제 + 뒤집기 |

## 배운 점

- 팰린드롬 판별은 "전처리(정제) + 비교" 두 단계로 나뉨
- Solution 1은 투 포인터로 직접 비교, Solution 2는 `[::-1]` 슬라이싱으로 간결하게 처리
