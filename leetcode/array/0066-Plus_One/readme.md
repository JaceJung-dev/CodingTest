# 66. Plus One

## 문제

- 링크: https://leetcode.com/problems/plus-one/
- 난이도: Easy
- 태그: Array, Math

## 접근 방식

- 사람이 계산하듯이 뒤에서부터 순회하며 계산
- 현재 자릿수가 9가 아니면 +1 하고 바로 return
- 9이면 0으로 바꾸고 다음 자릿수로 올림 전파
- 모든 자릿수가 9인 경우(예: `[9,9,9]`) 루프를 끝까지 돌고 `[1] + digits` 반환

## 풀이

```python
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
```

같은 로직을 carry 변수를 명시적으로 사용하여 표현:

```python
class Solution2:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)

        carry = 1
        for i in range(n - 1, -1, -1):
            tmp = digits[i] + carry
            digits[i] = tmp % 10
            carry = tmp // 10
        if carry:
            digits = [1] + digits

        return digits
```

## 복잡도

- 시간: O(n) — 최악의 경우 전체 순회 (모든 자릿수가 9)
- 공간: O(1) — in-place 수정 (모두 9인 경우만 O(n))

## 배운 점

- 올림이 발생하지 않는 순간 즉시 return하는 early exit 패턴으로 불필요한 순회를 제거
