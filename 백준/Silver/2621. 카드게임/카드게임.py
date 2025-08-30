import sys
from collections import Counter
input = sys.stdin.readline


colors = []
nums = []
for _ in range(5):
    color, num = input().split()
    colors.append(color)
    nums.append(int(num))

c_counts = Counter(colors)
n_counts = Counter(nums)
n_values = sorted(n_counts.values(), reverse=True)
max_num = max(nums)
min_num = min(nums)


is_straight = (len(set(nums)) == 5) and max_num - min_num == 4

if len(c_counts) == 1 and is_straight:
    print(max_num + 900)
elif n_values == [4, 1]:
    temp = next(k for k, v in n_counts.items() if v == 4)
    print(temp + 800)
elif n_values == [3, 2]:
    three = next(k for k, v in n_counts.items() if v == 3)
    two = next(k for k, v in n_counts.items() if v == 2)
    print(three * 10 + two + 700)
elif len(c_counts) == 1:
    print(max_num + 600)
elif is_straight:
    print(max_num + 500)
elif 3 in n_values:
    temp = next(k for k, v in n_counts.items() if v == 3)
    print(temp + 400)
elif n_values == [2, 2, 1]:
    temp = [k for k, v in n_counts.items() if v == 2]
    print(max(temp) * 10 + min(temp) + 300)
elif n_values == [2, 1, 1, 1]:
    temp = next(k for k, v in n_counts.items() if v == 2)
    print(temp + 200)
else:
    print(max_num + 100)