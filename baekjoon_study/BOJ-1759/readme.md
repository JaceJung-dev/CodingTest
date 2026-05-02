# BOJ 1759 - 암호 만들기

## 문제

- 링크: https://www.acmicpc.net/problem/1759
- 태그: 재귀, 백트래킹, 조합, 브루트포스

## 접근 방식

C개의 알파벳 중 L개를 골라 오름차순 암호를 만들되, 모음 1개 이상 + 자음 2개 이상 조건을 만족해야 함.
L개의 조합을 선택한 후 자음, 모음 개수 조건 확인.

두 가지 방식으로 구현:

1. **백트래킹 직접 구현** - 재귀로 조합 생성 후 조건 검증
2. **라이브러리 사용** - `itertools.combinations`로 조합 생성 후 조건 검증

## 풀이

### Solution 1 — 백트래킹

```python
def is_possible():
    global L, C, letters, selections
    v_cnt = 0
    for char in selections:
        v_cnt += char in vowels
    c_cnt = L - v_cnt
    return v_cnt >= 1 and c_cnt >= 2


def combination(index, level):
    if level == L:
        if is_possible():
            print("".join(selections))
        return

    for i in range(index, C):
        selections.append(letters[i])
        combination(i + 1, level + 1)
        selections.pop()
```

### Solution 2 — itertools.combinations

```python
def is_possible(arr):
    v_cnt = 0
    for char in arr:
        v_cnt += char in vowels
    c_cnt = L - v_cnt
    return v_cnt >= 1 and c_cnt >= 2


for comb in combinations(letters, L):
    if is_possible(comb):
        print("".join(comb))
```

### 공통

- `letters.sort()`로 사전순 정렬 → 조합이 자연스럽게 사전순으로 생성됨
- 모음 판별: `char in "aeiou"`

## 복잡도

- 시간: O(C(C, L)) — 모든 조합을 생성하고 각각 O(L) 검증
- 공간: O(L) — 재귀 깊이 및 selection 리스트

## 배운 점

- 조합 생성 + 조건 필터링 패턴: 모든 후보를 만들고 유효성 검사로 걸러내는 브루트포스 접근
- 입력을 미리 정렬하면 별도의 정렬 없이 사전순 출력 가능
