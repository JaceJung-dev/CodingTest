import sys
from collections import deque

input = sys.stdin.readline


def check_boxes(M, N, H):
    boxes = []
    for _ in range(H):
        plane = [list(map(int, input().split())) for _ in range(N)]
        boxes.append(plane)
    return boxes


def check_start_point(boxes, M, N, H):
    queue = deque([])
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if boxes[z][y][x] == 1:
                    queue.append((z, y, x))
    return queue


def bfs(boxes, queue, dirs, M, N, H):
    while queue:
        z, y, x = queue.popleft()

        for dz, dy, dx in dirs:
            n_z = z + dz
            n_y = y + dy
            n_x = x + dx

            if 0 <= n_z < H and 0 <= n_y < N and 0 <= n_x < M:
                if boxes[n_z][n_y][n_x] == 0:
                    boxes[n_z][n_y][n_x] = boxes[z][y][x] + 1
                    queue.append((n_z, n_y, n_x))


def calculate_days(boxes, M, N, H):
    max_day = 0

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if boxes[z][y][x] == 0:
                    return -1
                max_day = max(max_day, boxes[z][y][x])

    return max_day - 1


def main():
    M, N, H = map(int, input().split())

    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    boxes = check_boxes(M, N, H)
    queue = check_start_point(boxes, M, N, H)

    bfs(boxes, queue, dirs, M, N, H)

    days = calculate_days(boxes, M, N, H)
    print(days)


if __name__ == "__main__":
    main()
