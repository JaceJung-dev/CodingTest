import sys
input = sys.stdin.readline

def get_number_of_odd_even(cards):
    odd, even = 0, 0
    for card in cards:
        if card % 2 == 1:
            odd += 1
        else:
            even += 1
    return odd, even

while True:
    N = int(input())
    
    if N == 0:
        break
        
    M = list(map(int, input().split()))
    J = list(map(int, input().split()))
    MO, ME = get_number_of_odd_even(M)
    JO, JE = get_number_of_odd_even(J)
    
    odd_count = min(MO, JE) + min(ME, JO)
    print(N - odd_count)

    