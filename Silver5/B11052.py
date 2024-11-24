# 카드 구매하기
import sys

n = int(sys.stdin.readline())
card = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, n+1):
    for j in range(i):
        card[i] = max(card[i], card[j] + card[i-j]) # i = j + x -> x = i - j

print(card[n])
