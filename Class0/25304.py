# 영수증
x = int(input())
n = int(input())
T = 0

for i in range(n):
    a, b = map(int, input().split())
    T += a*b

if x == T:
    print("Yes")
else:
    print("No")