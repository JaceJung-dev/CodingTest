import sys

input = sys.stdin.readline

paid = int(input())

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
