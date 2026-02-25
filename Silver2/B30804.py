# 과일 탕후루
# 브루트포스 알고리즘
from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
counter = Counter()
start = 0
result = 0

for end in range(n):
    counter[s[end]] += 1 # 핵심

    while len(counter) > 2:
        counter[s[start]] -= 1

        if counter[s[start]] == 0:
            del counter[s[start]]  # 핵심

        start += 1

    result = max(result, end - start + 1)

print(result)
