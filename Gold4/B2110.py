# 공유기 설치
# 거리
n, c = map(int, input().split())
homes = sorted(int(input()) for _ in range(n))
start = 1  # 최소 거리
end = homes[-1] - homes[0]  # 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2

    # 첫번째 집에는 무조건 설치
    t = homes[0]
    cnt = 1

    for i in range(1, n):

        # 공유기 설치
        if homes[i] >= t + mid:
            cnt += 1
            t = homes[i]

    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
