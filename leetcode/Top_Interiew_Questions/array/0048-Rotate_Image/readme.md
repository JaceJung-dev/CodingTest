# 48. Rotate Image

## 문제

- 링크: https://leetcode.com/problems/rotate-image/
- 난이도: Medium
- 태그: Array, Math, Matrix

## 접근 방식

- 90도 시계 방향 회전 = 전치(transpose) + 좌우 반전(reverse)
- 1단계: 대각선 기준으로 swap하여 전치 (`matrix[i][j] ↔ matrix[j][i]`)
- 2단계: 각 행을 reverse
- 예: `[[1,2],[3,4]]` → 전치 `[[1,3],[2,4]]` → reverse `[[3,1],[4,2]]`

## 풀이

```python
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()
```

## 복잡도

- 시간: O(n²) — n x n 행렬 전체 순회
- 공간: O(1) — in-place swap

## 배운 점

- 행렬 90도 회전은 전치 + reverse라는 공식으로 외워두자
- `j`를 `i + 1`부터 시작해야 이미 swap한 원소를 다시 되돌리지 않음 (삼각형 절반)
- 반시계 방향 회전은 전치 + 상하 반전(각 열 reverse)
