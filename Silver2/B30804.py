# 과일 탕후루
from collections import Counter
import sys

n = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))
counter = Counter()
start = 0
result = 0

for end in range(n):
    counter[fruits[end]] += 1 # 핵심

    while len(counter) > 2:
        counter[fruits[start]] -= 1
        if counter[fruits[start]] == 0:
            del counter[fruits[start]]
        start += 1
    
    result = max(result, end - start + 1) # 핵심2

print(result)
