N = int(input())
before_bits = input()
after_bits = input()

is_success = True
if N % 2 == 0:
    if before_bits == after_bits:
        is_success = True
    else:
        is_success = False
else:
    for i in range(len(before_bits)):
        if before_bits[i] == after_bits[i]:
            is_success = False
            break

if is_success:
    print("Deletion succeeded")
else:
    print("Deletion failed")