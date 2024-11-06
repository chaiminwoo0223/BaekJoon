# 먹을 것인가 먹힐 것인가
# from bisect import bisect_right
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = sorted(map(int, sys.stdin.readline().split()))
    b = sorted(map(int, sys.stdin.readline().split()))
    count = 0
    
    for i in range(n):
        start = 0 # 인덱스 범위 시작
        end = m - 1 # 인덱스 범위 끝
        while start <= end:
            mid = (start + end) // 2
            if a[i] > b[mid]:
                start = mid + 1
            else:
                end = mid - 1
        count += start
    print(count)
