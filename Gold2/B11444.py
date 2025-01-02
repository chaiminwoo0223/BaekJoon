# 피보나치 수 6
# 도가뉴 항등식
import sys

n = int(sys.stdin.readline())
number = {} # 핵심
number[0] = 0
number[1] = 1
number[2] = 1

def fibonacci(n):
    m = n // 2
    if n in number:
        return number[n]
    elif n % 2 == 0:
        number[n] = (fibonacci(m) * (fibonacci(m) + 2 * fibonacci(m-1))) % 1000000007
    else:
        number[n] = (fibonacci(m+1)**2 + fibonacci(m)**2) % 1000000007
    return number[n]

print(fibonacci(n))
