import sys

input = sys.stdin.readline

# Solution 1

# input
paid = int(input())

# solve
change = 1000 - paid

count = 0
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


# Solution 2

# input
paid = int(input())

# solve
change = 1000 - paid

coins = [500, 100, 50, 10, 5, 1]

count = 0
for coin in coins:
    count += change // coin
    change %= coin

print(count)

# Solution 3

# input
paid = int(input())

# solve
change = 1000 - paid

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

print(count)
