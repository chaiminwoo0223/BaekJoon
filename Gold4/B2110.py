# 공유기 설치
# 거리
n, c = map(int, input().split())
distances = sorted(int(input()) for _ in range(n))
start = 1 # 최소 거리
end = distances[-1] - distances[0] # 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    point = distances[0]
    cnt = 1

    for i in range(1, n):
        if distances[i] - point >= mid:
            cnt += 1
            point = distances[i]

    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)