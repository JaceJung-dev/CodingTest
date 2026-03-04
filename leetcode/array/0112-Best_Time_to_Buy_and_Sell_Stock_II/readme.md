# 122. Best Time to Buy and Sell Stock II

## 문제

- 링크: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
- 난이도: Medium
- 태그: Array, Dynamic Programming, Greedy

## 접근 방식

- 여러 번 매수/매도 가능 → 오르는 구간의 이익을 모두 합산하면 최대 이익
- 연속된 두 날의 차이(`prices[i] - prices[i-1]`)가 양수이면 그 차이만큼 이익 누적
- Greedy: 복잡한 구간 계산 없이, 매일 "어제보다 올랐으면 판다"는 전략

## 풀이

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profits = 0
        for i in range(1, len(prices)):
            gap = prices[i] - prices[i - 1]
            if gap > 0:
                profits += gap

        return profits
```

## 복잡도

- 시간: O(n) — 배열을 한 번 순회
- 공간: O(1) — 변수 하나로 이익 누적

## 배운 점

- "여러 번 거래 가능"한 주식 문제는 모든 상승 구간의 합이 곧 최대 이익
- 연속 상승(1→2→3)을 한 번에 사는 것과 매일 사고파는 것의 이익이 동일 (3-1 == (2-1)+(3-2))
