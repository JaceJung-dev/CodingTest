import sys

input = sys.stdin.readline

base_table = {
    "A": {"A": "A", "G": "C", "C": "A", "T": "G"},
    "G": {"A": "C", "G": "G", "C": "T", "T": "A"},
    "C": {"A": "A", "G": "T", "C": "C", "T": "G"},
    "T": {"A": "G", "G": "A", "C": "G", "T": "T"},
}

N = int(input())
bases = input().strip()

base = bases[-1]

for i in range(N - 2, -1, -1):
    base = base_table[bases[i]][base]

print(base)
