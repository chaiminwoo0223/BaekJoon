# 다음 소수
from math import sqrt
import sys

def isPrime(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(sqrt(number))+1): # 에라토스테네스의 체
            if number % i == 0:
                return False
        return True

n = int(sys.stdin.readline().strip())

for _ in range(n):
    number = int(sys.stdin.readline().strip())

    while not isPrime(number):
        number += 1
    
    print(number)
