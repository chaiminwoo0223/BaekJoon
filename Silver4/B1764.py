# 듣보잡(집합)
n, m  = map(int, input().split())
D = set()
B = set()

for _ in range(n):
    D.add(input())

for _ in range(m):
    B.add(input())

print(len(D.intersection(B)))
for i in sorted(D.intersection(B)):
    print(i)