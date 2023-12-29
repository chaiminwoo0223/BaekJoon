# 평균
n = int(input())
score = list(map(int,input().split()))
M = max(score)

new_score = []
for i in range(n) :
    new_score.append(score[i]/M *100)
avg = sum(new_score)/n
print(avg)