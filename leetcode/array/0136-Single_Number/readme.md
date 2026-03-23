# 136. Single Number

## 문제

- 링크: https://leetcode.com/problems/single-number/
- 난이도: Easy
- 태그: Array, Bit Manipulation

## 접근 방식

- XOR 성질: `a ^ a = 0`, `a ^ 0 = a`, 교환/결합 법칙 성립
- 전체를 XOR하면 짝수 번 등장한 값은 상쇄되고 1번만 등장한 값만 남음

## 풀이

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_num = 0
        for num in nums:
            single_num ^= num

        return single_num
```

## 복잡도

- 시간: O(n) — 배열을 한 번 순회
- 공간: O(1) — 변수 하나만 사용

## 배운 점

- XOR은 "짝수 번 등장 제거" 패턴의 핵심 연산
