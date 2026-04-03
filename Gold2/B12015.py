# 가장 긴 증가하는 부분 수열 2
# 이분 탐색 + 다이나믹 프로그래밍
import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [0]

def binary_search(arr, x):
    start, end = 0, len(arr)

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return start

for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])

    if a[i] < dp[-1]:
        x = binary_search(dp, a[i])
        dp[x] = a[i]

print(len(dp)-1)
