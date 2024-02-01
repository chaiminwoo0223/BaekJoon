# 좌표 압축
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
unique_sorted = sorted(set(nums))
index_map = {num: idx for idx, num in enumerate(unique_sorted)}

for num in nums:
    print(index_map[num], end=' ')