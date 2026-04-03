# 189. Rotate Array

## 문제

- 링크: https://leetcode.com/problems/rotate-array/
- 난이도: Medium
- 태그: Array, Math, Two pointers

## 접근 방식

### Solution 1 — 새 배열

- 새 배열을 만들어 각 원소를 k칸 오른쪽으로 이동한 위치에 배치
- `(i + k) % n`으로 회전 후 인덱스 계산 (모듈러 연산으로 wraparound 처리)
- `nums[:] = new_arr`로 원본 배열에 in-place 반영

### Solution 2 — Reverse 3회

- `k %= n`으로 불필요한 회전 제거
- 전체 reverse → 앞 k개 reverse → 나머지 reverse
- 예: `[1,2,3,4,5,6,7]`, k=3 → `[7,6,5,4,3,2,1]` → `[5,6,7,4,3,2,1]` → `[5,6,7,1,2,3,4]`

## 풀이

### Solution 1

```python
class Solution1:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        new_arr = [0] * n

        for i in range(n):
            new_arr[(i + k) % n] = nums[i]

        nums[:] = new_arr
```

### Solution 2

```python
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

## 복잡도

|            | 시간 | 공간                    |
| ---------- | ---- | ----------------------- |
| Solution 1 | O(n) | O(n) — 새 배열 생성     |
| Solution 2 | O(n) | O(1) — in-place reverse |

## 배운 점

- 배열 회전의 핵심은 `(i + k) % n`으로 새 위치를 계산하는 것
- `nums[:] = new_arr`는 참조를 유지하면서 내용을 교체하는 파이썬 표현 (`nums = new_arr`는 참조만 바꿔서 원본에 영향 없음)
- Reverse 3회 기법은 공간 O(1)로 회전을 구현하는 고전적인 트릭
