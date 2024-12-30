# 피보나치 수 3
# 피사노 주기: 피보나치 수를 K로 나눈 나머지는 항상 주기를 가진다.
import sys

n = int(sys.stdin.readline())
n = n % (15 * 100000) # 피사노 주기를 P라고 했을 때, N % M == (N % P) % M
a, b = 0, 1

for _ in range(n-1):
    a, b = b % 1000000, (a + b) % 1000000
print(b)
