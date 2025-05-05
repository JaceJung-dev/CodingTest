def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

while True:
    n = input()
    if n == "0":
        break
    else:
        if is_palindrome(n):
            print("yes")
        else:
            print("no")
            