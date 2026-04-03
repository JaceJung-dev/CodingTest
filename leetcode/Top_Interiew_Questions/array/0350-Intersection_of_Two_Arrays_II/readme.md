# 350. Intersection of Two Arrays II

## 문제

- 링크: https://leetcode.com/problems/intersection-of-two-arrays-ii/
- 난이도: Easy
- 태그: Array, Hash Table, Two Pointers, Binary Search, Sorting

## 접근 방식

### Solution 1 — Counter (Hash Map)

- `Counter`로 nums1의 각 원소 등장 횟수를 기록
- nums2를 순회하면서 count가 남아있는 원소만 결과에 추가하고 count 차감

### Solution 2 — 정렬 + Two Pointers

- 두 배열을 정렬한 뒤 포인터 두 개로 동시 순회
- 값이 같으면 결과에 추가하고 둘 다 전진, 작은 쪽만 전진하여 따라잡기

## 풀이

### Solution 1

```python
from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        count = Counter(nums1)

        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result
```

### Solution 2

```python
class Solution2:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        result = []
        i, j = 0, 0
        len_nums1, len_nums2 = len(nums1), len(nums2)
        while i < len_nums1 and j < len_nums2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result
```

## 복잡도

|            | 시간           | 공간           |
| ---------- | -------------- | -------------- |
| Solution 1 | O(n + m)       | O(min(n, m))   |
| Solution 2 | O(n log n + m log m) | O(1) — 결과 배열 제외 |

## 배운 점

- `Counter`는 등장 횟수 기반 교집합 문제에 적합 (`&` 연산도 지원: `Counter(nums1) & Counter(nums2)`)
- 이미 정렬된 데이터라면 Solution 2가 추가 공간 없이 효율적
- set 교집합은 중복을 무시하지만, 이 문제는 등장 횟수를 보존해야 하므로 count 차감 or 투 포인터 방식이 필요
