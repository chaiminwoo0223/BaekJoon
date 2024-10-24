# 예산
import sys

n = int(sys.stdin.readline())
budgets = sorted(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
start, end = 0, budgets[-1] # 이진 탐색을 위한 초깃값 설정

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for budget in budgets:
        if budget < mid:
            total += budget
        else:
            total += mid
        
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
