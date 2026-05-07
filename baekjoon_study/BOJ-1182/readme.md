# BOJ 1182 - 부분수열의 합

## 문제

- 링크: https://www.acmicpc.net/problem/1182
- 태그: 브루트포스, 백트래킹, 부분집합

## 접근 방식

N개의 정수 중 크기가 양수인 부분수열의 합이 S가 되는 경우의 수를 구하는 문제. 각 원소를 선택/비선택하는 부분집합 탐색으로 접근. 세 가지 방식으로 구현:

1. **재귀 (리스트 저장)** - selections에 원소를 담아 합 비교
2. **재귀 (합 누적)** - cur_sum 변수로 합만 추적하여 메모리 절약
3. **라이브러리 사용** - `itertools.combinations`로 모든 크기의 조합 생성

## 풀이

### Solution 1 — 재귀 (리스트 저장)

```python
def partial_comb(level):
    global N, S, nums, selections, count

    # base case
    if level == N:
        if selections and sum(selections) == S:
            count += 1
        return

    # recursive case
    # choose current element
    selections.append(nums[level])
    partial_comb(level + 1)
    selections.pop()

    # not choose current element
    partial_comb(level + 1)
```

- `selections`가 비어있지 않고 합이 S이면 카운트
- 공집합 제외는 `selections` 비어있는지 체크로 처리

### Solution 2 — 재귀 (합 누적)

```python
def partial_comb2(level):
    global N, S, nums, cur_sum, count

    # base case
    if level == N:
        if cur_sum == S:
            count += 1
        return

    # recursive case
    # choose current element
    cur_sum += nums[level]
    partial_comb2(level + 1)
    cur_sum -= nums[level]

    # not choose current element
    partial_comb2(level + 1)
```

- 리스트 대신 `cur_sum` 변수로 합만 추적
- 공집합도 `cur_sum == S`를 만족할 수 있으므로, `S == 0`이면 `count -= 1`로 공집합 제외

### Solution 3 — itertools.combinations

```python
count = 0
for i in range(1, N + 1):
    for candidate in combinations(nums, i):
        if sum(candidate) == S:
            count += 1
```

- 크기 1부터 N까지 모든 조합을 생성하여 합이 S인 경우 카운트

## 복잡도

- 시간: O(2^N) — Solution 1, 2는 부분집합 탐색, Solution 3도 전체 조합 수의 합이 2^N - 1
- 공간: O(N) — 재귀 깊이 (Solution 1은 selections 리스트 추가)

## 배운 점

- 부분집합 탐색의 핵심: 각 원소를 **선택/비선택** 두 갈래로 재귀
- 공집합 처리 방식 차이: Solution 1은 `selections` 비어있는지 체크, Solution 2는 `S == 0`일 때 후처리로 `count -= 1`
- 합만 필요할 때는 리스트 저장 없이 누적 변수로 추적하는 게 효율적
