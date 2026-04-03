# 7. Reverse Integer

## 문제

- 링크: https://leetcode.com/problems/reverse-integer/
- 난이도: Medium
- 태그: Math

## 접근 방식

### Solution 1 — 문자열 뒤집기

- 정수를 문자열로 변환 후 `[::-1]`로 뒤집기
- 음수는 부호를 분리한 뒤 처리하고 다시 붙임
- 32비트 정수 범위 초과 시 0 반환

### Solution 2 — 수학적 자릿수 추출

- `x % 10`으로 마지막 자릿수를 꺼내고 `result * 10 +`으로 쌓아감
- `x //= 10`으로 한 자리씩 줄여가며 반복
- 문자열 변환 없이 숫자 연산만으로 해결

## 풀이

### Solution 1

```python
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            x *= -1
            result = int(str(x)[::-1]) * -1
        else:
            result = int(str(x)[::-1])

        if result > 2**31 - 1 or result < -(2**31):
            return 0

        return result
```

### Solution 2

```python
class Solution2:
    def reverse(self, x: int) -> int:
        is_negative = False
        result = 0

        if x < 0:
            is_negative = True
            x *= -1

        while x > 0:
            result = result * 10 + x % 10
            x //= 10

        result = result * -1 if is_negative else result

        if result > 2**31 - 1 or result < -(2**31):
            return 0

        return result
```

## 복잡도

|            | 시간     | 공간                   |
| ---------- | -------- | ---------------------- |
| Solution 1 | O(log x) | O(log x) — 문자열 변환 |
| Solution 2 | O(log x) | O(1)                   |

- 자릿수 = log₁₀(x)이므로 시간은 둘 다 O(log x)

## 배운 점

- 파이썬 `[::-1]`은 간편하지만, Solution 2처럼 수학적 접근 가능
- `x % 10`으로 꺼내고 `result * 10`으로 쌓는 패턴은 정수 자릿수 조작의 기본기
- 32비트 오버플로우 체크(`-2³¹ ~ 2³¹-1`)는 이 유형 문제의 필수 조건
