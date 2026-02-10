# 예산
n = int(input())
pays = sorted(map(int, input().split()))
m = int(input())
start, end = 0, pays[-1] # 핵심

while start <= end:
    mid = (start + end) // 2
    t = 0

    for pay in pays:
        if pay < mid:
            t += pay
        else:
            t += mid

    if t <= m:
        start = mid + 1
    else:
        end = mid - 1

    print(start, end, mid)

print(end)
