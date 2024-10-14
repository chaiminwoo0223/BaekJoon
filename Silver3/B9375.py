# 패션왕 신해빈
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    result = 1
    fashion = {}

    for _ in range(n):
        item, category = map(str, sys.stdin.readline().strip().split())
        if category in fashion:
            fashion[category] += 1
        else:
            fashion[category] = 1

    for category in fashion:
        result *= (fashion[category] + 1) # 핵심
        
    print(result - 1) # 아무 것도 선택하지 않는 경우 제거
