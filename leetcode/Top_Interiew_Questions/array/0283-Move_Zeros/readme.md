# 283. Move Zeroes

## 문제

- 링크: https://leetcode.com/problems/move-zeroes/
- 난이도: Easy
- 태그: Array, Two Pointers

## 접근 방식

### Solution 1 — 덮어쓰기 + 나머지 0 채우기

- 0이 아닌 값을 앞에서부터 순서대로 덮어쓰기
- 순회 후 write 이후 나머지 자리를 0으로 채움

### Solution 2 — Swap

- 0이 아닌 값을 발견하면 `nums[read]`과 `nums[write]`를 swap
- swap 방식이라 별도로 0을 채우는 후처리가 불필요

## 풀이

### Solution 1

```python
class Solution:
    def moveZeros(self, nums: list[int]) -> None:
        n = len(nums)
        write = 0

        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        for i in range(write, n):
            nums[i] = 0
```

### Solution 2

```python
class Solution2:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        write = 0

        for read in range(n):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
```

## 복잡도

- 시간: O(n) — 배열을 한 번 순회 (둘 다 동일)
- 공간: O(1) — in-place 처리 (둘 다 동일)

## 배운 점

- read/write 투 포인터 패턴
- Solution 1은 대입 + 후처리, Solution 2는 swap으로 한 번에 처리 — swap이 더 깔끔
