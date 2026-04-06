# 가장 긴 증가하는 부분 수열 5
from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# LIS의 길이를 유지하기 위한 배열
lis = []

# 각 원소가 lis 배열의 어느 인덱스에 들어갔는지 기록
record = [0] * n

for i in range(n):
    if not lis or a[i] > lis[-1]:
        lis.append(a[i])
        record[i] = len(lis) - 1
    else:
        idx = bisect_left(lis, a[i]) # 이분 탐색으로 들어갈 위치 찾기
        lis[idx] = a[i]
        record[i] = idx

# record를 뒤에서부터 훑으며 실제 수열 찾기
result = []
target = len(lis) - 1

for i in range(n-1, -1, -1):
    if record[i] == target:
        result.append(a[i])
        target -= 1

print(len(lis)) # LIS 길이 출력
print(*result[::-1]) # 역추적
