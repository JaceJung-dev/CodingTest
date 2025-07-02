def solution(board):
    answer = 0
    mines = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for i2 in range(i-1, i+2):
                    if 0 <= i2 <= n-1:
                        for j2 in range(j-1, j+2):
                            if 0 <= j2 <= n-1:
                                mines.append((i2, j2))
    mines_set = set(mines)
    answer = n * n - len(mines_set)
    return answer