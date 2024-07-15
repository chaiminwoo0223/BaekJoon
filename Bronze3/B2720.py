# 세탁소 사장 동혁
import sys

t = int(sys.stdin.readline().strip())
coins = [25, 10, 5, 1]

for _ in range(t):
    c = int(sys.stdin.readline().strip())
    result = []

    for coin in coins:
        result.append(c // coin)
        c %= coin
    
    print(" ".join(map(str, result)))
