# 덩치
n = int(input())
num = []

for i in range(n):
    x, y = map(int, input().split())
    num.append([x, y])

for j in num: # 핵심: 2중 for문을 활용하여, 각각의 숫자를 뽑아서 비교한다.
    rank = 1
    for k in num:
        if (j[0] < k[0]) and (j[1] < k[1]):
            rank += 1
    print(rank, end=' ')        