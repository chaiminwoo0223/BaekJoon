# DNA
from collections import Counter
import sys

n, m = map(int, sys.stdin.readline().split())
dna = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
result = ""
total = 0

for j in range(m):
    counter = Counter()

    for i in range(n):
        counter[dna[i][j]] += 1

    best = sorted(counter.most_common(), key = lambda x:(-x[1], x[0]))
    result += best[0][0]
    total += n - best[0][1]

print(result)
print(total)
