import sys

input = sys.stdin.readline

sentence = input().strip().upper()

happy_char = set("HAPPY")
sad_char = set("SAD")

h_point = 0
s_point = 0

for char in sentence:
    if char in happy_char:
        h_point += 1
    if char in sad_char:
        s_point += 1

happiness_index = 5000

if not (h_point == 0 and s_point == 0):
    temp = (h_point * 100000) // (h_point + s_point)

    if temp % 10 >= 5:
        temp += 10

    happiness_index = temp // 10

print(f"{happiness_index * 0.01:.2f}")
