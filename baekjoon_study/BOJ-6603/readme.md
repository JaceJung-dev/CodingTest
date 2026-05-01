# BOJ 6603 - 로또

## 문제

- 링크: https://www.acmicpc.net/problem/6603
- 태그: 재귀, 백트래킹, 조합

## 접근 방식

K개의 수 중 6개를 고르는 조합 문제. 두 가지 방식으로 구현:

1. **직접 구현 (백트래킹)** - 재귀로 조합을 직접 생성
2. **라이브러리 사용** - `itertools.combinations` 활용

## 풀이

### Solution 1 — 백트래킹 직접 구현

```python
def combination(index, level):
    if level == 6:
        print(*selection)
        return

    for i in range(index, K):
        selection.append(S[i])
        combination(i + 1, level + 1)
        selection.pop()
```

### Solution 2 — itertools.combinations

```python
for comb in combinations(S, 6):
    print(*comb)
```

### 공통

- 입력이 `0`이면 종료하는 반복 구조
- 각 테스트 케이스 사이에 빈 줄 출력

## 복잡도

- 시간: O(C(K, 6)) — K개 중 6개를 고르는 조합의 수
- 공간: O(6) — 재귀 깊이 및 selection 리스트

## 배운 점

- 백트래킹의 핵심 패턴: `append → 재귀 → pop`
- `index` 파라미터로 탐색 시작점을 제한하면 자연스럽게 오름차순 조합이 생성됨
- `itertools.combinations`와 직접 구현의 결과가 동일함을 확인
