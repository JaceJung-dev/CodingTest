# BOJ 10974 - 모든 순열

## 문제

- 링크: https://www.acmicpc.net/problem/10974
- 태그: 재귀, 백트래킹, 순열, 브루트포스

## 접근 방식

1부터 N까지의 모든 순열을 사전순으로 출력. 두 가지 방식으로 구현:

1. **백트래킹 직접 구현** - `check` 배열로 사용 여부를 추적하며 재귀
2. **라이브러리 사용** - `itertools.permutations` 활용

## 풀이

### Solution 1 — 백트래킹

```python
def permutation(level):
    if level == N:
        print(*selections)
        return

    for i in range(1, N):
        if check[i]:
            continue

        check[i] = True
        selections.append(i)
        permutation(level + 1)

        selections.pop()
        check[i] = False
```

### Solution 2 — itertools.permutations

```python
for permutation in permutations(range(1, N + 1), N):
    print("".join(map(str, permutation)))
```

## 복잡도

- 시간: O(N! × N) — N!개의 순열을 각각 N길이로 출력
- 공간: O(N) — 재귀 깊이, selections, check 배열

## 배운 점

- 순열과 조합의 백트래킹 차이: 조합은 `index`로 시작점을 제한하지만, 순열은 `check` 배열로 사용 여부를 관리
- 0부터 순회하되 `i + 1`을 저장하여 1~N 범위를 자연스럽게 처리
