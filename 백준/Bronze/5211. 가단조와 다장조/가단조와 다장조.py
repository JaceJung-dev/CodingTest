import sys

music = list(sys.stdin.readline().rstrip().split("|"))

major = ["C", "F", "G"]
minor = ["A", "D", "E"]
major_count = 0
minor_count = 0

for bar in music:
    if bar[0] in major:
        major_count += 1
    elif bar[0] in minor:
        minor_count += 1
        
if major_count > minor_count:
    print("C-major")
elif major_count < minor_count:
    print("A-minor")
else:
    if music[-1][-1] in major:
        print("C-major")
    elif music[-1][-1] in minor:
        print("A-minor")