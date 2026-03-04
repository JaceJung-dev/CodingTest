# 26. Remove Duplicates from Sorted Array

## 문제

- 링크: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- 난이도: Easy
- 태그: Array, Two Pointer

## 접근 방식

- Two Pointer (read/write) 패턴으로 in-place 처리
  - `write`: 다음에 고유 값을 쓸 위치
  - `read`: 배열을 순회하며 이전 값과 다른 값을 탐색
- `nums[read] != nums[read - 1]`이면 새로운 고유 값 → `nums[write]`에 기록 후 `write++`

## 풀이

```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write
```

## 복잡도

- 시간: O(n) — 배열을 한 번 순회
- 공간: O(1) — 추가 메모리 없이 in-place 수정

## 배운 점

- 정렬된 배열에서 중복 제거는 read/write 투 포인터의 대표적인 활용 사례
- in-place 수정 문제에서는 "어디에 쓸지(write)"와 "어디를 읽을지(read)"를 분리하는 게 핵심
