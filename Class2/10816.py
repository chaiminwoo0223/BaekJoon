# 숫자 카드 2
n = int(input())
num_1 = sorted(list(map(int, input().split())))
m = int(input())
num_2 = list(map(int, input().split()))
cnt = {} # 핵심

for i in num_1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for j in num_2:
    if j in cnt:
        print(cnt[j], end=" ")
    else:
        print(0, end=" ")