import sys

input = sys.stdin.readline

while True:
    try:
        N, M = map(int, input().split())
        
        count = 0

        for num in range(N, M + 1):
            num_str = str(num)
            
            if len(num_str) == len(set(num_str)):
                count += 1

        print(count)

    except:
        break

