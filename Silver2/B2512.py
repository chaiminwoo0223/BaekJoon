# 예산
n = int(input())
pays = sorted(map(int, input().split()))
m = int(input())
start, end = 0, pays[-1]

while start <= end:
    mid = (start + end) // 2
    result = 0

    for pay in pays:
        if pay < mid:
            result += pay
        else:
            result += mid

    if result <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
