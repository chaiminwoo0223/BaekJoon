# 거스름돈
import sys

n = int(sys.stdin.readline())
balance = 1000 - n
count = 0

for coin in [500, 100, 50, 10, 5, 1]:
    if balance // coin > 0:
        count += balance // coin
        balance = balance % coin
    
print(count)
