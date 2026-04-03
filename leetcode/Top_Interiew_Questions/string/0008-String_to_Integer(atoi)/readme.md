# 8. String to Integer (atoi)

## 문제

- 링크: https://leetcode.com/problems/string-to-integer-atoi/
- 난이도: Medium
- 태그: String

## 접근 방식

- 문제 조건을 순서대로 처리하는 상태 기반 파싱
  1. 앞쪽 공백 건너뛰기 (`while s[i] == " "`)
  2. 부호 판별 (`+` / `-`)
  3. 연속된 숫자를 `res * 10 + digit`으로 누적
  4. 매 단계에서 32비트 정수 범위 클램핑

## 풀이

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return 0

        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit

            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX

            i += 1

        return sign * res
```

## 복잡도

- 시간: O(n) — 문자열을 한 번 순회
- 공간: O(1) — 변수만 사용

## 배운 점

- atoi 문제는 알고리즘보다 엣지 케이스 처리가 핵심 (공백, 부호, 오버플로우, 비숫자 문자)
- 조건을 순서대로 나열하면 자연스럽게 풀리는 파싱 문제 유형
- 숫자 누적 시 매번 범위 체크를 해야 오버플로우를 조기에 잡을 수 있음
