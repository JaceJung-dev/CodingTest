# 1. Two Sum

## 문제

- 링크: https://leetcode.com/problems/two-sum/
- 난이도: Easy
- 태그: Array, Hash Table

## 접근 방식

### Solution 1 — Brute Force

- 이중 루프로 모든 쌍을 비교

### Solution 2 — Hash Map (Two-pass)

- 1차 순회: 모든 값과 인덱스를 Hash Map에 저장
- 2차 순회: complement가 Hash Map에 있는지 탐색
- 자기 자신과 매칭되지 않도록 `num_map[complement] != i` 체크

### Solution 3 — Hash Map (One-pass)

- 순회하면서 동시에 Hash Map을 채움
- complement가 이미 저장되어 있으면 바로 반환

## 풀이

### Solution 1

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
```

### Solution 2

```python
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        num_map = {}

        for i in range(n):
            num_map[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]

        return []
```

### Solution 3

```python
class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
```

## 복잡도

|            | 시간  | 공간 |
| ---------- | ----- | ---- |
| Solution 1 | O(n²) | O(1) |
| Solution 2 | O(n)  | O(n) |
| Solution 3 | O(n)  | O(n) |

## 배운 점

- Brute Force → Two-pass Hash → One-pass Hash 순으로 최적화 과정을 연습할 수 있는 대표 문제
- Solution 2는 먼저 전체를 저장 후 탐색, Solution 3은 저장과 탐색을 동시에 수행하여 한 번의 패스로 해결
