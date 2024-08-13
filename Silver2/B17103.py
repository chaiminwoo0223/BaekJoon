# 골드바흐 파티션
import sys

def Prime(max_num):
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    return primes

def GoldbachPartition(num, primes):
    count = 0
    for i in range(2, num//2+1):
        j = num - i
        if primes[i] and primes[j]:
            count += 1
    print(count)

t = int(sys.stdin.readline().strip())
max_num = 1000000
primes = Prime(max_num)

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    GoldbachPartition(n, primes)
