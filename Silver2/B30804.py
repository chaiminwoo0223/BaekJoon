# 과일 탕후루
# 브루트포스 알고리즘
# Counter
from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))
counter = Counter()
start = 0
result = 0

for end in range(n):
    counter[fruits[end]] += 1 # 핵심

    print(counter)

    while len(counter) > 2: # 핵심
        counter[fruits[start]] -= 1

        if counter[fruits[start]] == 0:
            del counter[fruits[start]]

        start += 1

    result = max(result, end + 1 - start)

print(result)
