import sys
input = sys.stdin.readline

N, K = map(int, input().split())
costs = list(map(int, input().split()))
bids = list(map(int, input().split()))
min_cost = min(costs)

max_count = 0
for mask in range(1 << 6):
    budget = K
    count = 0
    for bid in bids:
        if (mask >> (bid - 1)) & 1:
            cost = costs[bid - 1]
            if budget >= cost:
                budget -= cost
                count += 1
            if budget < min_cost:
                break
                
    if count > max_count:
        max_count = count
        
print(max_count)