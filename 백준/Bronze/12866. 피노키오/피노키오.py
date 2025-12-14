import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

gene = input().strip().upper()

genelist = ["A", "C", "G", "T"]
gene_count = Counter(gene)
total_count = 1

for base in genelist:
    count = gene_count.get(base, 0)
    total_count *= count

print(total_count % 1000000007)
