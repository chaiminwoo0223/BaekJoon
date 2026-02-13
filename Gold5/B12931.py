# 두 배 더하기
n = int(input())
b = list(map(int, input().split()))
cnt = 0

while True:
    # 1) 배열에 있는 값 하나를 1 증가시킨다.
    for i in range(n):
        if b[i] % 2 == 1:
            b[i] -= 1
            cnt += 1

    if max(b) == 0:
        print(cnt)
        break

    # 2) 배열에 있는 모든 값을 두 배 시킨다.
    for i in range(n):
        b[i] //= 2

    cnt += 1
