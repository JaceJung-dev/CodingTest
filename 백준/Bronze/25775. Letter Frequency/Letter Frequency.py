import sys
from collections import defaultdict, Counter

def get_max_letter(l_list):
    l_list.sort()
    max_letter = []
    counts = Counter(l_list)
    
    max_count = max(counts.values())

    for i, v in counts.items():
        if v == max_count:
            max_letter.append(i)
            
    return " ".join(max_letter)

input = sys.stdin.readline

letter_counts = defaultdict(list)

N = int(input())
for _ in range(N):
    word = input().rstrip()
    
    for i in range(len(word)):
        letter_counts[i+1].append(word[i])
        
for i, v in letter_counts.items():
    max_letter = get_max_letter(v)
    
    print(f"{i}: {max_letter}")
    