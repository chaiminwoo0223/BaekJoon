# 나이순 정렬
n = int(input())
result = []
for i in range(n):
    a, b = map(str, input().split())
    result.append([int(a), i, b]) # 핵심
result.sort()

for j in range(n):
    print(result[j][0], result[j][2])