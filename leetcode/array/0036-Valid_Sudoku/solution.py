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


class Solution2:
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
