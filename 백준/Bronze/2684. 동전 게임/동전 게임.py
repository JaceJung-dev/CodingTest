import sys
from collections import Counter
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    cases = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, 
             "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
    
    coin_toss = input().rstrip()
    for i in range(len(coin_toss) - 2):
        case = coin_toss[i:i+3]
        cases[case] += 1
        
    answer_list = list(cases.values())
    print(*answer_list)
    