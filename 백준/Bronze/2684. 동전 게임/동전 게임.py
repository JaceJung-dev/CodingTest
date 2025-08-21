import sys
input = sys.stdin.readline

P = int(input())
ref = ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]

for _ in range(P):
    coin_toss = input().rstrip()
    count = [0] * 8
    
    for i in range(len(coin_toss) - 2):
        case = coin_toss[i: i + 3]
        count[ref.index(case)] += 1
        
    print(*count)