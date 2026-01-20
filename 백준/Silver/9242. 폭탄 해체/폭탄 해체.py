import sys

input = sys.stdin.readline

DIGITS = {
    ("***", "* *", "* *", "* *", "***"): 0,
    ("  *", "  *", "  *", "  *", "  *"): 1,
    ("***", "  *", "***", "*  ", "***"): 2,
    ("***", "  *", "***", "  *", "***"): 3,
    ("* *", "* *", "***", "  *", "  *"): 4,
    ("***", "*  ", "***", "  *", "***"): 5,
    ("***", "*  ", "***", "* *", "***"): 6,
    ("***", "  *", "  *", "  *", "  *"): 7,
    ("***", "* *", "***", "* *", "***"): 8,
    ("***", "* *", "***", "  *", "***"): 9,
}

codes = [input().rstrip("/n") for _ in range(5)]

num_count = (len(codes[0]) + 1) // 4

is_not_digit = False
digit_list = []
for i in range(num_count):
    start = i * 4
    code = tuple(code[start : start + 3] for code in codes)
    if code not in DIGITS:
        is_not_digit = True
        break
    digit_list.append(DIGITS[code])

if is_not_digit:
    print("BOOM!!")
else:
    last_digit = digit_list[-1]
    digit_sum = sum(digit_list)
    if last_digit % 2 == 0 and digit_sum % 3 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")
