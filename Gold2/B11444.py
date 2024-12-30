# 피보나치 수 6
# 도가뉴 항등식
import sys

n = int(sys.stdin.readline())
mod = 1000000007
number = {}
number[0] = 0
number[1] = 1
number[2] = 1

def fibonacci(n):
    k = n // 2
    if n in number:
        return number[n]
    elif n % 2 == 0: # n = 2k
        number[n] = (fibonacci(k) * (fibonacci(k) + 2 * fibonacci(k-1))) % mod
    else: # n = 2k + 1
        number[n] = (fibonacci(k+1)**2 + fibonacci(k)**2) % mod
    return number[n]

print(fibonacci(n))
