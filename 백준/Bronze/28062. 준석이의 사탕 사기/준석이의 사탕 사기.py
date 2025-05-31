N = int(input())
candies = list(map(int, input().split()))

candies.sort()

if sum(candies) % 2 == 1:
    for candy in candies:
        if candy % 2 == 1:
            candies.remove(candy)
            break

if sum(candies) % 2 == 1:
    print(0)
else:
    print(sum(candies))

    
        
    