n = int(input())
word = input()

letter_count = [word.count(i) for i in "usopc"]

print(min(letter_count))