# 제곱근
import sys

n = int(sys.stdin.readline())

start = 0 # 인덱스 범위 시작
end = n # 인덱스 범위 끝

while start <= end:
    mid = (start + end) // 2
    if n > mid**2:
        start = mid + 1
    else:
        end = mid
        if n == mid**2:
            break

print(mid)
