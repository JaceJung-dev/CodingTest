# BOJ 1018 - 체스판 다시 칠하기

## 문제

- 링크: https://www.acmicpc.net/problem/1018
- 태그: 브루트포스 알고리즘

## 접근 방식

N×M 보드(N, M ≤ 50)에서 모든 8×8 부분판을 시작점 `(si, sj)`로 잡고, 두 종류의 체스판 패턴(좌상단이 B인 것 / W인 것) 중 더 적게 칠해야 하는 횟수의 최솟값을 구함.

- 부분판 개수: 최대 `(50-7) × (50-7) ≈ 1,849`
- 각 부분판 검사: 64칸 → 전체 약 12만 연산으로 충분

두 가지 접근:

- **풀이 1**: 좌상단 칸을 기준 색으로 잡고 한 패턴만 카운트 → 반대 패턴은 `64 - count`로 한 번에 처리
- **풀이 2**: 정답 체스판 두 종류(`chess1`, `chess2`)를 미리 만들어두고 각 부분판과 직접 비교

## 풀이

### Solution 1 — 좌상단 기준 + `64 - count` 트릭

```python
import sys

input = sys.stdin.readline

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
```

- `(i+j) % 2 == 0` 칸은 좌상단(`start`)과 같은 색이어야 → 다르면 칠하기
- `(i+j) % 2 == 1` 칸은 좌상단과 달라야 → 같으면 칠하기
- `count`는 "좌상단을 `start` 색으로 두는 패턴"의 칠하기 횟수, 반대 패턴은 정확히 `64 - count`
- 두 값과 기존 최솟값을 한 번에 `min`으로 비교

### Solution 2 — 정답 체스판 템플릿 두 개와 직접 비교

```python
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
```

- `chess1` = 좌상단 B인 정답 체스판, `chess2` = 좌상단 W인 정답 체스판
- 각 부분판마다 두 정답 패턴과 칸별로 비교해 다른 칸 수(`case1`, `case2`)를 셈
- 두 값 중 작은 쪽이 그 부분판의 최소 비용
- `si + 7 >= N or sj + 7 >= M` 으로 8×8이 안 들어가는 시작점은 스킵

## 복잡도

|            | 시간                | 공간     |
| ---------- | ------------------- | -------- |
| Solution 1 | O((N−7)(M−7) · 64)  | O(N · M) |
| Solution 2 | O((N−7)(M−7) · 64)  | O(N · M) |

- N, M ≤ 50 → 최악 약 12만 연산, 어느 풀이든 충분

## 배운 점

- N, M이 작은 격자 문제는 **모든 시작점 × 부분판 내부 전수 검사**로도 충분
- "두 패턴 중 작은 쪽" 같은 이항 선택은 **한 패턴만 세고 `total - count`** 로 다른 쪽을 동시에 얻을 수 있음 → 검사 횟수가 절반
- 직관적으로 풀고 싶다면 **정답 체스판 두 개를 직접 만들어두고 비교** 하는 방식이 코드가 명시적이라 디버깅하기 쉬움
- 두 접근은 본질적으로 같은 연산량(부분판당 64 비교), 다만 메모리 접근 패턴과 가독성이 다름
