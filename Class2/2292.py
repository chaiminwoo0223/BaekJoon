# 벌집
n = int(input())
count = 1
hexagon = 1

while n > hexagon:
    hexagon += 6*count # 핵심
    count += 1
print(count)