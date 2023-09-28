# 주사위 세개
d1, d2, d3 = list(map(int, input().split()))

if (d1 == d2 == d3):
    price = 10000 + (d1 * 1000)
elif (d1 == d2) or (d1 == d3):
    price = 1000 + (d1 * 100)
elif (d2 == d1) or (d2 == d3):
    price = 1000 + (d2 * 100)
elif (d3 == d1) or (d3 == d2):
    price = 1000 + (d3 * 100)
else:
    price = max(d1, d2, d3) * 100

print(price)