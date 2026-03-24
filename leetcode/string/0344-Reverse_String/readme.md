# 344. Reverse String

## 문제

- 링크: https://leetcode.com/problems/reverse-string/
- 난이도: Easy
- 태그: Two Pointers, String

## 접근 방식

- 양 끝에서 시작하는 Two Pointer (left/right)
- 두 포인터가 만날 때까지 swap하며 안쪽으로 이동

## 풀이

```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

## 복잡도

- 시간: O(n) — 배열 절반만 순회
- 공간: O(1) — in-place swap

## 배운 점

- 양 끝에서 좁혀오는 투 포인터의 가장 기본적인 형태
- Array의 Rotate Array(189번)의 reverse 함수와 동일한 패턴
