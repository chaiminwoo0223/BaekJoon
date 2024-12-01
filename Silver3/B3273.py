# 두 수의 합
# 투 포인터
# 정렬
import sys

n = int(sys.stdin.readline())
numbers = sorted(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
start = 0
end = n-1
count = 0

while start < end:
    result = numbers[start] + numbers[end]

    if result == x:
        count += 1
        start += 1
        end -= 1
    elif result < x:
        start += 1
    else:
        end -= 1

print(count)
