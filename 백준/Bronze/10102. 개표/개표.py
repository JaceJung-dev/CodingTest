import sys

input = sys.stdin.readline

a_count, b_count = 0, 0
N = int(input())
votes = input().strip().upper()

for vote in votes:
    if vote == "A":
        a_count += 1
    else:
        b_count += 1
        
if a_count > b_count:
    print("A")
elif a_count < b_count:
    print("B")
else:
    print("Tie")
        
