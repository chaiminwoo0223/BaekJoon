# 좌표 정렬하기
n = int(input())
array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append([x, y])
array.sort()

for j in array:
    print(j[0], j[1])