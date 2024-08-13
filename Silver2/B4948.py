# 베르트랑 공준
import sys

num = 123456*2+1
primes = [1]*num
for i in range(1, num):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            primes[i] = 0
            break

while True:
    n = int(sys.stdin.readline().strip())
    if(n == 0):
        break
    else:
        count = 0
        for i in range(n+1, 2*n+1):
            count += primes[i]
        print(count)
