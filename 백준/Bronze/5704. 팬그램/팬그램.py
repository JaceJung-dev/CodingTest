import sys

input = sys.stdin.readline

alphabets = set("abcdefghijklmnopqrstuvwxyz")

while True:
    sentence = "".join(input().split())

    if sentence == "*":
        break

    sentence_set = set(sentence)

    if sentence_set == alphabets:
        print("Y")
    else:
        print("N")
