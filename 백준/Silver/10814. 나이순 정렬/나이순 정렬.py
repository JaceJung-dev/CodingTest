import sys
input = sys.stdin.readline

N = int(input())
people = [input().split() for _ in range(N)]
    
people.sort(key=lambda x: int(x[0]))

for person in people:
    print(" ".join(person))


    