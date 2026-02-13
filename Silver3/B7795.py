# 먹을 것인가 먹힐 것인가
# 이분탐색
# 인덱스
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    cnt = 0

    for num in a:
        start = 0
        end = m - 1

        while start <= end:
            mid = (start + end) // 2

            if num > b[mid]:
                start = mid + 1
            else:
                end = mid - 1

        cnt += start

    print(cnt)
