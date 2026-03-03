# 과일 탕후루
# 브루트포스 알고리즘
from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
counter = Counter()
t = 0 # 핵심
result = 0

for i in range(n):
    counter[s[i]] += 1 # 핵심

    while len(counter) > 2:
        counter[s[t]] -= 1 # 핵심

        if counter[s[t]] == 0:
            del counter[s[t]]

        t += 1

    result = max(result, i - t + 1)

print(result)
