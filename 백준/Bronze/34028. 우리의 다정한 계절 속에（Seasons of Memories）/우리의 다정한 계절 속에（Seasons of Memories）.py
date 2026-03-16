import sys

input = sys.stdin.readline


def get_season_gap(year, month):
    if month == 1 or month == 2:
        season_gap = 0
    elif 3 <= month <= 5:
        season_gap = 1
    elif 6 <= month <= 8:
        season_gap = 2
    elif 9 <= month <= 11:
        season_gap = 3
    else:
        year += 1
        season_gap = 0

    return (year - 2015) * 4 + season_gap


A, B, C = map(int, input().split())

print(get_season_gap(A, B) + 1)
