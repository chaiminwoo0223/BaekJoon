# 가장 긴 증가하는 부분 수열 3
# 이분 탐색 + 다이나믹 프로그래밍
import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
result = [a[0]]

def binary_search(start, end, target):
    if start > end:
        return start

    mid = (start + end) // 2

    if result[mid] > target:
        return binary_search(start, mid-1, target)
    elif result[mid] < target:
        return binary_search(mid+1, end, target)
    else:
        return mid

for i in range(1, n):
    if result[-1] < a[i]:
        result.append(a[i])
    else:
        result[binary_search(0, len(result)-1, a[i])] = a[i]

print(len(result))
