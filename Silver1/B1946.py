# 신입 사원
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    numbers = sorted(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    count = 0
    interview = n
    
    for x, y in numbers:
        if y < interview: # 핵심
            count += 1
            interview = y
            print(x, y, count)
        
    print(count)
