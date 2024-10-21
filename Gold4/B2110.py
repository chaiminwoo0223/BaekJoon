# 공유기 설치
import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
houses = sorted(int(sys.stdin.readline()) for _ in range(n)) # 정렬된 리스트
start = 1 # 가능한 최소 거리
end = houses[-1] - houses[0] # 가능한 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2 # 중간값: 공유기 간의 후보 거리
    current = houses[0]
    count = 1 # 첫번째 집에 첫번째 공유기 설치

    # 최소 mid 거리 이상으로 공유기 설치
    for i in range(1, n):
        if houses[i] - current >= mid:
            count += 1
            current = houses[i]

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
