import sys

input = sys.stdin.readline

# Solution 1

# input
N, M = map(int, input().split())
matrix = [input().strip() for _ in range(N)]

# solve
min_count = 64
for si in range(N - 7):
    for sj in range(M - 7):
        count = 0
        start = matrix[si][sj]

        for i in range(8):
            for j in range(8):
                cur = matrix[si + i][sj + j]
                if (i + j) % 2 == 0 and cur != start:
                    count += 1
                if (i + j) % 2 == 1 and cur == start:
                    count += 1

        min_count = min(min_count, count, 64 - count)

print(min_count)

# Solution 2


def get_min(si, sj):
    case1, case2 = 0, 0

    for i in range(8):
        for j in range(8):
            case1 += matrix[si + i][sj + j] != chess1[i][j]
            case2 += matrix[si + i][sj + j] != chess2[i][j]

    return min(case1, case2)


# initial setting
chess1 = [["" for _ in range(8)] for _ in range(8)]
chess2 = [["" for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        chess1[i][j] = "B" if (i + j) % 2 == 0 else "W"
        chess2[i][j] = "W" if (i + j) % 2 == 0 else "B"

# input
N, M = map(int, input().split())
matrix = [input().strip() for _ in range(N)]

min_count = 64
for si in range(N):
    for sj in range(M):
        if si + 7 >= N or sj + 7 >= M:
            continue
        min_count = min(min_count, get_min(si, sj))

print(min_count)
