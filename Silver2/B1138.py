# 한 줄로 서기
# 작은 사람부터
import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
result = [0] * n

for i in range(n):
    count = 0
    for j in range(n): # 핵심
        if result[j] == 0:
            count += 1
        if count == heights[i] + 1:
            result[j] = i + 1
            break
print(*result)
