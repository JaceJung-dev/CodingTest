import sys
from collections import deque

input = sys.stdin.readline


def solution():
    """입력을 받아서 정리하고, 단지의 크기를 계산에 형식에 맞게 출력"""
    N = int(input())
    town = [list(map(int, input().rstrip())) for _ in range(N)]
    checked = [[False] * N for _ in range(N)]

    # 단지별 크기를 계산에 오름차순으로 저장
    group_size_list = get_group_size_list(N, town, checked)

    # 형식에 맞게 출력
    print(len(group_size_list))
    for n in group_size_list:
        print(n)


def get_group_size_list(N, town, checked):
    """전체 지도들 돌면서 단지의 크기를 계산해 정렬된 리스트로 반환"""

    group_size_list = []

    for i in range(N):
        for j in range(N):
            # 해당 좌표에 집이 있고, 체크한 적이 없음 -> 단지의 시작(bfs시작)
            if town[i][j] == 1 and not checked[i][j]:
                group_size = bfs_calc_size(i, j, town, checked, N)
                group_size_list.append(group_size)

    return sorted(group_size_list)


def bfs_calc_size(start_i, start_j, town, checked, N):
    """하나의 단지가 시작하는 시작점에서 bfs로 단지의 크기를 계산함."""
    checked[start_i][start_j] = True
    group = deque([(start_i, start_j)])
    group_size = 1
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 인접한 집 (상하좌우)

    while group:
        x, y = group.popleft()

        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy
            # 새로운 좌표가 범위를 벗어난 경우 -> 건너뜀
            if not (0 <= new_x < N and 0 <= new_y < N):
                continue

            # 새로운 좌표에 집이 있고, 체크한 적이 없는 경우 -> queue에 집어넣기
            if town[new_x][new_y] == 1 and not checked[new_x][new_y]:
                checked[new_x][new_y] = True
                group.append((new_x, new_y))
                group_size += 1

    return group_size


if __name__ == "__main__":
    solution()
