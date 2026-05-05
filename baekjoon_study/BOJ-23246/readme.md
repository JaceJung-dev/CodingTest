# BOJ 23246 - Sport Climbing Combined

## 문제

- 링크: https://www.acmicpc.net/problem/23246
- 태그: 정렬

## 접근 방식

선수들을 다중 기준으로 정렬하여 상위 3명의 번호를 출력. 정렬 기준:

1. 세 과목 점수의 **곱** 오름차순
2. 곱이 같으면 세 과목 점수의 **합** 오름차순
3. 합도 같으면 **번호** 오름차순

## 풀이

```python
def comp(x):
    return (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0])


N = int(input())
players = [tuple(map(int, input().split())) for _ in range(N)]

players = sorted(players, key=comp)

for b, p, q, r in players[:3]:
    print(b, end=" ")
print()
```

- `comp` 함수가 `(곱, 합, 번호)` 튜플을 반환하여 다중 키 정렬
- `sorted()` 후 상위 3명의 번호만 출력

## 복잡도

- 시간: O(N log N) — 정렬
- 공간: O(N) — 선수 리스트 저장

## 배운 점

- `key` 함수에서 튜플을 반환하면 다중 정렬 기준을 간결하게 표현 가능
- 이전 11650 문제는 튜플 기본 비교로 충분했지만, 파생 값(곱, 합) 기준 정렬은 커스텀 `key` 함수가 필요
