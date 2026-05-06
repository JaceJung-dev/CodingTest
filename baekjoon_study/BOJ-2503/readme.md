# BOJ 2503 - 숫자 야구

## 문제

- 링크: https://www.acmicpc.net/problem/2503
- 태그: 브루트포스, 백트래킹, 순열

## 접근 방식

1~9 중 서로 다른 3자리 수의 모든 순열을 후보로 생성한 뒤, 각 질문의 스트라이크/볼 조건을 만족하는 후보만 카운트. 두 가지 방식으로 구현:

1. **백트래킹 직접 구현** - 재귀로 순열을 생성하여 candidates에 저장
2. **라이브러리 사용** - `itertools.permutations`로 순열 생성

## 풀이

### Solution 1 — 백트래킹

```python
def permutation(level):
    if level == 3:
        candidates.append(tmp[:])
        return

    for i in range(9):
        if check[i]:
            continue
        tmp.append(i + 1)
        check[i] = True
        permutation(level + 1)
        tmp.pop()
        check[i] = False


check = [False for _ in range(9)]
tmp = []
candidates = []

permutation(0)

count = 0
for candidate in candidates:
    is_ok = True
    for num, st, bl in queries:
        cur_st, cur_bl = 0, 0
        for i in range(3):
            if str(candidate[i]) == num[i]:
                cur_st += 1
            elif str(candidate[i]) in num:
                cur_bl += 1
        if cur_st != int(st) or cur_bl != int(bl):
            is_ok = False
            break
    if is_ok:
        count += 1
```

### Solution 2 — itertools.permutations

```python
count = 0
for candidate in permutations(range(1, 10), 3):
    is_ok = True
    for num, st, bl in queries:
        cur_st, cur_bl = 0, 0
        for i in range(3):
            if str(candidate[i]) == num[i]:
                cur_st += 1
            elif str(candidate[i]) in num:
                cur_bl += 1
        if cur_st != int(st) or cur_bl != int(bl):
            is_ok = False
            break
    if is_ok:
        count += 1
```

### 공통 검증 로직

- 같은 자리에 같은 숫자 → 스트라이크
- 다른 자리에 포함된 숫자 → 볼
- 모든 질문의 스트라이크/볼이 일치하면 유효한 후보

## 복잡도

- 시간: O(P(9,3) × N × 3) = O(504N) — 9P3 = 504개 후보 × N개 질문 × 3자리 비교
- 공간: O(P(9,3)) — 후보 리스트 (Solution 1), Solution 2는 O(1)

## 배운 점

- 브루트포스에서 후보 수가 충분히 작으면(504개) 전수 검사가 효율적
- 스트라이크/볼 판별: 자리 일치 → 스트라이크, 값만 포함 → 볼 (순서 주의, `elif`로 중복 카운트 방지)
- `tmp[:]`로 리스트 복사하여 candidates에 저장해야 백트래킹 시 값이 보존됨
