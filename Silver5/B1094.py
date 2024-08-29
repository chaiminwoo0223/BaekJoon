# 막대기
import sys

bars = [64, 32, 16, 8, 4, 2, 1] # 핵심
count = 0
x = int(sys.stdin.readline())

for i in range(len(bars)):
    if x >= bars[i]:
        count += 1
        x -= bars[i]
    if x == 0:
        break

print(count)
