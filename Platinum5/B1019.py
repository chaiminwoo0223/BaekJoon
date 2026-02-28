# 책 페이지
import sys

input = sys.stdin.readline

n = int(input())
result = [0] * 10
start, point = 1, 1

def calculator(x, p):
    while x > 0:
        result[x % 10] += p
        x //= 10

while True:
    # n의 끝자리를 9로 맞추며 부족한 부분 직접 계산
    while n % 10 != 9 and start <= n:
        calculator(n, point)
        n -= 1

    if n < start:
        break

    # start의 끝자리를 0으로 맞추며 부족한 부분 직접 계산
    while start % 10 != 0 and start <= n:
        calculator(start, point)
        start += 1

    # 한 자릿수 아래로 내려가기 전, 0 ~ 9까지 공통 등장 횟수 합산
    start //= 10
    n //= 10

    for i in range(10):
        result[i] += n * point

    point *= 10

print(*result)
