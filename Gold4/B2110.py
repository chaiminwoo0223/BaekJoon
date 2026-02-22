# 공유기 설치
n, c = map(int, input().split())
x = sorted(int(input()) for _ in range(n))
start = 1 # 최소 거리
end = x[-1] - x[0] # 최대 거리

while start <= end:
    mid = (start + end) // 2
    point = x[0]
    cnt = 1

    for i in range(1, n):
        if x[i] >= point + mid:
            point = x[i]
            cnt += 1

    if cnt >= c:
        start = mid + 1
    else:
        end = mid - 1

print(end)
