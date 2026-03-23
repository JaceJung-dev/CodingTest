# 36. Valid Sudoku

## 문제

- 링크: https://leetcode.com/problems/valid-sudoku/
- 난이도: Medium
- 태그: Array, Hash Table, Matrix

## 접근 방식

### Solution 1 — 헬퍼 함수 분리

- 행, 열, 3x3 박스 각각에 대해 검증하는 함수 사용
- 각 함수에서 set으로 중복 여부를 체크

### Solution 2 — 단일 순회 + 튜플 키

- 9x9 보드를 한 번만 순회
- `("row", row, value)`, `("col", col, value)`, `("box", row//3, col//3, value)` 튜플을 하나의 set에 저장
- 이미 존재하는 키가 있으면 중복 → invalid

## 풀이

### Solution 1

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in range(9):
            if not self.is_valid_row(board, row):
                return False

        for col in range(9):
            if not self.is_valid_col(board, col):
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.is_valid_box(board, row, col):
                    return False
        return True

    def is_valid_row(self, board: list[list[str]], row: int) -> bool:
        seen = set()

        for col in range(9):
            val = board[row][col]
            if val == ".":
                continue
            if val in seen:
                return False

            seen.add(val)

        return True

    def is_valid_col(self, board: list[list[str]], col: int) -> bool:
        seen = set()

        for row in range(9):
            val = board[row][col]
            if val == ".":
                continue
            if val in seen:
                return False

            seen.add(val)

        return True

    def is_valid_box(self, board: list[list[str]], row: int, col: int) -> bool:
        seen = set()

        for box_row in range(row, row + 3):
            for box_col in range(col, col + 3):
                val = board[box_row][box_col]
                if val == ".":
                    continue
                if val in seen:
                    return False

                seen.add(val)

        return True

```

### Solution 2

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                row_key = ("row", row, value)
                col_key = ("col", col, value)
                box_key = ("box", row // 3, col // 3, value)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True
```

## 복잡도

|            | 시간  | 공간                                |
| ---------- | ----- | ----------------------------------- |
| Solution 1 | O(81) | O(9) — 각 검증마다 set 생성/해제    |
| Solution 2 | O(81) | O(81) — 모든 키를 하나의 set에 저장 |

- 보드 크기가 9x9로 고정이므로 둘 다 사실상 O(1)

## 배운 점

- 튜플을 set 키로 활용하면 행/열/박스 검증을 하나의 set + 단일 순회로 통합 가능
- Solution 1은 가독성이 좋고, Solution 2는 코드가 간결하고 순회가 한 번이라 효율적
