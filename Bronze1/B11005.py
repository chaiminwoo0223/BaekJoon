# 진법 변환 2
import sys

# 입력 받기
n, b = map(int, sys.stdin.readline().strip().split())
result = ''
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# n 진수 변환
while n > 0:
    result += str(number[n%b])
    n //= b

# 결과 출력
print(result[::-1])
