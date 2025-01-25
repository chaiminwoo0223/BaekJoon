# 신입 사원
# float('inf')
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ranking = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]) # 핵심
    count = 0
    interview = float('inf')
    
    for _, y in ranking:
        if y < interview: # 핵심
            count += 1
            interview = y
        
    print(count)
