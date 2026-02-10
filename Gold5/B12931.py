# 두 배 더하기
n = int(input())
a = [0] * n
b = list(map(int, input().split()))
cnt = 0

while True:
    # 더하기 연산
    for i in range(n):
        if b[i] % 2 == 1:
            b[i] -= 1
            cnt += 1

    if max(b) == 0:
        print(cnt)
        break

    # 곱하기 연산
    for i in range(n):
        b[i] //= 2

    cnt += 1
