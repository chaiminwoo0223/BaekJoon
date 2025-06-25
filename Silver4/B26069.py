# 붙임성 좋은 총총이
n = int(input())
dancer = {"ChongChong"}

for i in range(n):
    a, b = input().split()

    if a in dancer and b not in dancer:
        dancer.add(b)
    if b in dancer and a not in dancer:
        dancer.add(a)

print(len(dancer))
