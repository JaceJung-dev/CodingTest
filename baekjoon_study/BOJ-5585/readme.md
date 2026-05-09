# BOJ 5585 - 거스름돈

## 문제

- 링크: https://www.acmicpc.net/problem/5585
- 태그: 그리디

## 접근 방식

1000엔에서 물건 값을 뺀 거스름돈을 최소 동전 수로 만드는 문제. 세 가지 방식으로 구현:

1. **그리디 (직접 계산)** - 큰 동전부터 하나씩 나눗셈/나머지 연산
2. **그리디 (반복문)** - 동전 배열을 순회하며 동일 로직을 간결하게
3. **브루트포스** - 모든 동전 조합을 탐색하여 최솟값

## 풀이

### Solution 1 — 그리디 (직접 계산)

```python
change = 1000 - paid

c_500 = change // 500
change %= 500
c_100 = change // 100
change %= 100
c_50 = change // 50
change %= 50
c_10 = change // 10
change %= 10
c_5 = change // 5
c_1 = change % 5

print(c_500 + c_100 + c_50 + c_10 + c_5 + c_1)
```

### Solution 2 — 그리디 (반복문)

```python
coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
    count += change // coin
    change %= coin

print(count)
```

### Solution 3 — 브루트포스

```python
count = int(1e8)

for c_500 in range(2):
    for c_100 in range(10):
        for c_50 in range(20):
            for c_10 in range(100):
                for c_5 in range(200):
                    value = c_500 * 500 + c_100 * 100 + c_50 * 50 + c_10 * 10 + c_5 * 5
                    if change - value >= 0:
                        count = min(
                            count, c_500 + c_100 + c_50 + c_10 + c_5 + (change - value)
                        )
```

- 5중 루프로 모든 동전 조합을 탐색, 나머지를 1원 동전으로 채워 최솟값 갱신

## 복잡도

| | 시간 | 공간 |
| --- | --- | --- |
| Solution 1, 2 | O(1) — 동전 종류 수(6)만큼 | O(1) |
| Solution 3 | O(2 × 10 × 20 × 100 × 200) | O(1) |

## 배운 점

- 동전 단위가 서로 배수 관계일 때 그리디가 최적해를 보장함
- Solution 1의 반복 패턴을 배열 + 반복문(Solution 2)으로 리팩토링하면 코드가 훨씬 간결
- Solution 3은 그리디가 왜 효율적인지 대비하기 위한 브루트포스 비교용
