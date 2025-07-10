N = int(input())
before = input().strip()
after = input().strip()

if N % 2 == 0:
    result = before == after
else:
    result = all(b1 != b2 for b1, b2 in zip(before, after))

print("Deletion succeeded" if result else "Deletion failed")
