# 두 수의 합
# 투 포인터(범위 축소)
# 정렬
import sys

n = int(sys.stdin.readline())
a = sorted(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
start = 0
end = n-1
count = 0

while start < end:
    number = a[start] + a[end]

    if number < x:
        start += 1
    elif number > x:
        end -= 1
    else:
        start += 1
        end -= 1
        count += 1

print(count)
