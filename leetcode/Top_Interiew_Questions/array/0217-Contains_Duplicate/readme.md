# 217. Contains Duplicate

## 문제

- 링크: https://leetcode.com/problems/contains-duplicate/
- 난이도: Easy
- 태그: Array, Hash Table, Sorting

## 접근 방식

### Solution 1 — Set 길이 비교

- 배열을 set으로 변환 후 길이 비교
- 길이가 다르면 중복 존재

### Solution 2 — Brute Force

- 이중 루프로 모든 쌍을 비교

### Solution 3 — 정렬 후 인접 비교

- 정렬하면 중복 원소가 연속으로 위치
- 인접한 원소만 비교하면 됨

### Solution 4 — Set 순회

- 순회하면서 set에 저장, 이미 있으면 중복
- Solution 1과 달리 중복 발견 즉시 early return

### Solution 5 — Hash Map 카운트

- dict로 등장 횟수를 기록하며 순회
- 이미 1번 이상 등장한 값이 나오면 중복

## 풀이

### Solution 1

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set(nums)
        if len(nums) != len(nums_set):
            return True
        else:
            return False
```

### Solution 2

```python
class Solution2:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False
```

### Solution 3

```python
class Solution3:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True

        return False
```

### Solution 4

```python
class Solution4:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False
```

### Solution 5

```python
class Solution5:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            else:
                seen[num] = seen.get(num, 0) + 1

        return False
```

## 복잡도

|            | 시간       | 공간 |
| ---------- | ---------- | ---- |
| Solution 1 | O(n)       | O(n) |
| Solution 2 | O(n²)      | O(1) |
| Solution 3 | O(n log n) | O(1) |
| Solution 4 | O(n)       | O(n) |
| Solution 5 | O(n)       | O(n) |

## 배운 점

- Solution 1은 간결하지만 항상 전체를 set으로 변환, Solution 4는 early return으로 최선의 경우 더 빠름
- Solution 3의 정렬 방식은 추가 공간 없이 O(n log n)으로 풀 수 있는 중간 지점
