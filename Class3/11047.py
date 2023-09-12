# 동전 0
n, k = map(int, input().split())
coin = []
cnt = 0

for _ in range(n):
    coin.append(int(input()))

for i in reversed(range(n)):
    cnt += k // coin[i]
    k = k % coin[i]
print(cnt)