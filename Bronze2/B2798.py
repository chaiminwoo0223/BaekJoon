# 블랙잭
from itertools import combinations

n, m = map(int, input().split())
N = list(map(int, input().split()))
result = 0
for i in combinations(N, 3):
    if sum(i) > m:
        continue
    else:
        result = max(sum(i), result) # 핵심
print(result)
