# 피보나치 수 2
import sys

n = int(sys.stdin.readline())
number = [0] * 91
number[1] = 1

if n > 1:
    for i in range(2, n+1):
        number[i] = number[i-1] + number[i-2]
        
print(number[n])
