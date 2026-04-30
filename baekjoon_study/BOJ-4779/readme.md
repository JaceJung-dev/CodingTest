# BOJ 4779 - 칸토어 집합

## 문제

- 링크: https://www.acmicpc.net/problem/4779
- 태그: 재귀, 분할 정복, 문자열

## 접근 방식

길이 `3^N`의 문자열에서 가운데 1/3을 공백으로 바꾸는 작업을 재귀적으로 반복. 세 가지 방식으로 구현:

1. **반복문 (Bottom-up)** - 미리 테이블을 만들어 조회
2. **재귀 (출력)** - `cantor(n)`: 재귀하며 직접 `print`
3. **재귀 (문자열 반환)** - `cantor2(n)`: 재귀하며 문자열을 조합하여 반환

## 풀이

### Solution 1 — Bottom-up 테이블

```python
ans = ["" for _ in range(13)]
ans[0] = "-"

for i in range(1, 13):
    ans[i] = ans[i - 1] + " " * 3 ** (i - 1) + ans[i - 1]

while True:
    try:
        N = int(input())
        print(ans[N])
    except:
        break
```

### Solution 2 — 재귀 (직접 출력)

```python
def cantor(n):
    if n == 0:
        print("-", end="")
        return
    cantor(n - 1)
    print(" " * 3 ** (n - 1), end="")
    cantor(n - 1)
```

### Solution 3 — 재귀 (문자열 반환)

```python
def cantor2(n):
    if n == 0:
        return "-"
    return cantor2(n - 1) + " " * 3 ** (n - 1) + cantor2(n - 1)
```

### 공통

- EOF까지 입력을 받는 `try-except` 패턴

## 복잡도

- 시간: O(3^N) — 결과 문자열의 길이
- 공간: O(3^N) — 문자열 저장 (Solution 1은 모든 단계를 캐싱하므로 총 O(3^12))

## 배운 점

- 칸토어 집합의 재귀 구조: `왼쪽 + 공백 + 오른쪽`으로 분할 정복 패턴과 동일
- Bottom-up 테이블 방식은 재귀 호출 없이 반복 입력에 효율적
- 재귀에서 직접 출력 vs 문자열 반환의 트레이드오프: 출력 방식은 메모리 절약, 반환 방식은 코드가 깔끔
