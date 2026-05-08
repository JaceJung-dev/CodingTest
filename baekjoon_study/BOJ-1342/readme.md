# BOJ 1342 - 행운의 문자열

## 문제

- 링크: https://www.acmicpc.net/problem/1342
- 태그: 백트래킹, 순열, 브루트포스

## 접근 방식

문자열을 재배열하여 인접한 문자가 같지 않은 순열(행운의 문자열)의 수를 구하는 문제. 두 가지 방식으로 구현:

1. **라이브러리 + 중복 제거** - `itertools.permutations`로 전수 검사 후 중복 문자 팩토리얼로 나누기
2. **백트래킹 (카운터)** - 각 문자의 남은 개수를 추적하며 인접 조건을 pruning

## 풀이

### Solution 1 — itertools.permutations + 중복 제거

```python
count = 0
for perm in permutations(S):
    for i in range(len(S) - 1):
        if perm[i] == perm[i + 1]:
            break
    else:
        count += 1

for char in range(ord("a"), ord("z") + 1):
    count //= fact(S.count(chr(char)))
```

- 모든 순열을 생성하여 인접 조건 검사 (`for-else` 패턴)
- 중복 문자의 팩토리얼로 나눠 동일한 순열을 제거

### Solution 2 — 백트래킹 (카운터)

```python
def func(level):
    global S, chars, counter, selections, count
    if level == len(S):
        count += 1
        return

    for char in chars:
        if counter[char] == 0:
            continue

        if (not selections) or selections[-1] != char:
            selections.append(char)
            counter[char] -= 1
            func(level + 1)
            selections.pop()
            counter[char] += 1
```

- `counter`로 각 문자의 잔여 개수를 관리
- `selections[-1] != char` 조건으로 인접 중복을 pruning
- 중복 문자가 있어도 `chars`(set)로 순회하므로 자연스럽게 중복 순열 방지

## 복잡도

|            | 시간                                   | 공간 |
| ---------- | -------------------------------------- | ---- |
| Solution 1 | O(N! × N)                              | O(N) |
| Solution 2 | O(N!) 최악, pruning으로 실제 훨씬 적음 | O(N) |

## 배운 점

- 중복 문자가 있는 순열에서 `set`으로 고유 문자만 순회 + `counter`로 개수 관리하면 중복 없이 탐색 가능
- `for-else` 패턴: `break` 없이 루프가 끝나면 `else` 블록 실행 — 조건 위반 검사에 유용
- Solution 1는 전수 검사 후 수학적 중복 제거, Solution 2은 pruning으로 불필요한 탐색을 조기 차단,
