# BOJ 11650 - 좌표 정렬하기

## 문제

- 링크: https://www.acmicpc.net/problem/11650
- 태그: 정렬

## 접근 방식

2차원 좌표를 x좌표 기준 오름차순, x가 같으면 y좌표 기준 오름차순으로 정렬. Python 튜플의 기본 비교 연산이 이 조건과 동일하므로 `sorted()`만으로 해결.

## 풀이

```python
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points = sorted(points)

for x, y in points:
    print(x, y)
```

- 좌표를 `tuple`로 입력받아 리스트에 저장
- `sorted()`로 정렬 — 튜플은 첫 번째 원소 → 두 번째 원소 순으로 비교하므로 별도 key 불필요
- 정렬된 결과를 순회하며 출력

## 복잡도

- 시간: O(N log N) — Timsort
- 공간: O(N) — 좌표 리스트 저장

## 배운 점

- Python 튜플의 사전순 비교가 다중 키 정렬 조건과 일치하면 별도 `key` 함수 없이 `sorted()`만으로 충분
- 좌표를 `tuple`로 저장하면 불변성 + 비교 연산을 자연스럽게 활용 가능
