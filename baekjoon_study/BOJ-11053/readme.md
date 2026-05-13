# BOJ 11053 - 가장 긴 증가하는 부분 수열

## 문제

- 링크: https://www.acmicpc.net/problem/11053
- 태그: DP, LIS

## 접근 방식

수열에서 가장 긴 증가하는 부분 수열(LIS)의 길이를 구하는 문제.

- `dp[n]` = n번째 원소를 마지막으로 하는 LIS의 길이
- 점화식: `dp[n] = max(dp[i]) + 1` (단, `i < n`이고 `nums[i] < nums[n]`)

두 가지 방식으로 구현:

1. **Bottom-up DP** - 반복문으로 작은 인덱스부터 채워나감
2. **Top-down DP (메모이제이션)** - 재귀 + dp 배열 캐싱

## 풀이

### Solution 1 — Bottom-up DP

```python
N = int(input())
nums = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for n in range(1, N + 1):
    best = 0
    for i in range(1, n):
        if nums[n] > nums[i]:
            best = max(best, dp[i])
    dp[n] = best + 1

print(max(dp))
```

- 각 n마다 1~n-1까지 순회하며 `nums[i] < nums[n]`인 dp 값 중 최대를 찾아 +1
- 자기 자신만으로도 길이 1이므로 `best = 0`에서 시작

### Solution 2 — Top-down DP (메모이제이션)

```python
def func(n):
    if dp[n] != -1:
        return dp[n]

    best = 0
    for i in range(1, n):
        if nums[n] > nums[i]:
            best = max(best, func(i))

    dp[n] = best + 1

    return dp[n]
```

- `dp[n] != -1`이면 캐시 반환
- 재귀로 이전 값들을 채우며 동일한 점화식 적용

## 복잡도

- 시간: O(N²) — 각 n마다 이전 원소들을 모두 확인
- 공간: O(N) — dp 배열

## 배운 점

- LIS의 기본 DP 점화식: "현재 원소를 끝으로 하는 부분 수열 중 최장 길이"로 상태 정의
- O(N²) 방식 외에도 이분 탐색을 활용한 O(N log N) 방식이 존재 (`bisect.bisect_left` 활용)
- Top-down과 Bottom-up이 동일한 점화식이지만, 이 문제는 Bottom-up이 더 직관적
