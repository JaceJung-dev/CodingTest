# BOJ 1461 - 도서관

## 문제

- 링크: https://www.acmicpc.net/problem/1461
- 태그: 그리디, 정렬

## 접근 방식

0번 위치에서 출발하여 책을 원래 자리에 놓으러 가는 최소 걸음 수를 구하는 문제. 핵심 아이디어:

1. 양수/음수 위치를 분리하여 같은 방향 책끼리 묶기
2. 한 번에 M권씩 들고 갈 수 있으므로, 가장 먼 책부터 M개씩 그룹화
3. 각 그룹은 가장 먼 책까지 왕복(×2)해야 하지만, 마지막에 가장 먼 그룹은 돌아올 필요 없음(-max)

## 풀이

```python
N, M = map(int, input().split())
locations = list(map(int, input().split()))

pos = []
neg = []
for location in locations:
    if location > 0:
        pos.append(location)
    else:
        neg.append(-location)

pos = sorted(pos, reverse=True)
neg = sorted(neg, reverse=True)

dists = []

for p in pos[::M]:
    dists.append(p)

for n in neg[::M]:
    dists.append(n)

print(2 * sum(dists) - max(dists))
```

- 양수/음수를 분리하고 절댓값 내림차순 정렬
- `[::M]` 슬라이싱으로 M개씩 그룹의 대표(최댓값)만 추출
- 모든 그룹 왕복 거리 합 `2 * sum(dists)`에서 가장 먼 그룹 편도 `max(dists)`를 빼기

## 복잡도

- 시간: O(N log N) — 정렬
- 공간: O(N) — 양수/음수 분리 리스트

## 배운 점

- 방향별로 분리 후 그룹화하는 그리디 패턴: 같은 방향은 한 번에 처리하는 게 최적
- `[::M]` 슬라이싱으로 그룹 대표값을 간결하게 추출
- 마지막 이동은 돌아올 필요 없으므로 `- max(dists)`로 최적화하는 아이디어
