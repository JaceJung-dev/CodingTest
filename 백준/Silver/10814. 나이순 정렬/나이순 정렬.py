import sys

people = sys.stdin.readlines()[1:]
people.sort(key=lambda x: int(x.split()[0]))
print("".join(people))


    