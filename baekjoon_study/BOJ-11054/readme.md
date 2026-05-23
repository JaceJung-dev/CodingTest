# BOJ 11054 - 가장 긴 바이토닉 부분 수열

## 문제

- 링크: https://www.acmicpc.net/problem/11054
- 태그: 다이나믹 프로그래밍

## 접근 방식

바이토닉 수열은 어떤 인덱스 `k`에서 정점을 찍고 **증가하다가 감소**하는 형태. 핵심 관찰:

- `dp1[i]` = i번째 원소를 **마지막**으로 하는 가장 긴 **증가** 부분 수열의 길이 (LIS, 좌→우)
- `dp2[i]` = i번째 원소를 **시작**으로 하는 가장 긴 **감소** 부분 수열의 길이 (LIS를 우→좌로 본 것 = LDS)
- 정점이 `i`인 바이토닉 길이 = `dp1[i] + dp2[i] - 1` (i가 양쪽에서 한 번씩 세지므로 -1)

전형적인 LIS 점화식 (`O(N²)`)을 두 방향으로 두 번 돌리면 됨. N ≤ 1000이라 충분.

## 풀이

### Solution 1 — Bottom-Up (양방향 LIS)

```python
import sys

input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))

dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)
dp1[1], dp2[N] = 1, 1

for n in range(1, N + 1):
    dp1[n] = 1
    for i in range(1, n):
        if nums[n] > nums[i]:
            dp1[n] = max(dp1[n], dp1[i] + 1)

for n in range(N - 1, 0, -1):
    dp2[n] = 1
    for i in range(N, n, -1):
        if nums[n] > nums[i]:
            dp2[n] = max(dp2[n], dp2[i] + 1)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, dp1[i] + dp2[i] - 1)

print(ans)
```

- `nums = [0] + ...`로 1-indexed 처리
- `dp1`은 좌→우로, `dp2`는 우→좌로 LIS를 채움 (우→좌에서 `nums[n] > nums[i]`이므로 자연스럽게 LDS와 같음)
- 마지막에 정점을 `i`로 하는 모든 후보의 최댓값을 답으로

### Solution 2 — Top-Down (메모이제이션)

```python
def func1(n):

    if dp1[n] != -1:
        return dp1[n]

    dp1[n] = 1
    for i in range(1, n):
        if nums[n] > nums[i]:
            dp1[n] = max(dp1[n], func1(i) + 1)

    return dp1[n]


def func2(n):

    if dp2[n] != -1:
        return dp2[n]

    dp2[n] = 1
    for i in range(N, n, -1):
        if nums[n] > nums[i]:
            dp2[n] = max(dp2[n], func2(i) + 1)

    return dp2[n]


N = int(input())
nums = [0] + list(map(int, input().split()))

dp1 = [-1] * (N + 1)
dp2 = [-1] * (N + 1)
dp1[1], dp2[N] = 1, 1

ans = 0
for i in range(1, N + 1):
    ans = max(ans, func1(i) + func2(i) - 1)

print(ans)
```

- 메모 미스(`-1`)일 때만 재귀 → 동일 인덱스 한 번만 계산
- `func1`은 좌측 LIS, `func2`는 우측 LDS

## 복잡도

| | 시간 | 공간 |
| --- | --- | --- |
| Solution 1 | O(N²) | O(N) |
| Solution 2 | O(N²) | O(N) |

- N ≤ 1000 → O(N²) = 10⁶ 으로 충분 여유

## 배운 점

- "정점을 기준으로 좌/우 분할" 류의 문제는 **양방향 DP**로 푸는 것이 정석: 좌측에서 한 번, 우측에서 한 번 채우고 결합
- LDS는 LIS를 **방향만 뒤집어 같은 점화식**으로 처리 가능 → 별도 알고리즘 필요 없음
- 결합할 때 정점이 양쪽에 한 번씩 세어진다는 점에서 **-1 보정** 잊지 말기
- N ≤ 10⁵ 이상이라면 `O(N log N)` LIS(이분 탐색)를 양방향으로 적용해야 함 — 이번 문제는 N ≤ 1000이라 그대로 O(N²)로 OK
