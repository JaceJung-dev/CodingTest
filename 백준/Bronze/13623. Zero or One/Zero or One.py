A, B, C = map(int,input().split())

if A == B:
    if A == C:
        print("*")
    else:
        print("C")
elif A == C:
    if A != B:
        print("B")
elif B == C:
    if A != B:
        print("A")
else:
    print("*")           