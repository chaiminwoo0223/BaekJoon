# 랜선 자르기
# 이분탐색
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
start, end = 1, max(arr) 

while start <= end: # 핵심1
    mid = (start+end)//2
    len = 0 # 핵심2
    for i in range(k):
        len += arr[i]//mid
    if len >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)