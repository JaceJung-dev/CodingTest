import sys

music = list(sys.stdin.readline().rstrip().split("|"))

major = {"C", "F", "G"}
minor = {"A", "D", "E"}
major_count = 0
minor_count = 0

for bar in music:
    first = bar[0]
    if first in major:
        major_count += 1
    elif first in minor:
        minor_count += 1
        
if major_count > minor_count:
    print("C-major")
elif major_count < minor_count:
    print("A-minor")
else:
    last = music[-1][-1]
    print("C-major" if last in major else "A-minor")