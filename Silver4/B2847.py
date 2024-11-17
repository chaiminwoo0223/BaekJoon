# 게임을 만든 동준이
# 이전 점수보다 1 작은 값으로 줄이기
# 항상 답이 존재하는 경우만 주어진다.
import sys

n = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(n)]
count = 0

for i in range(n-2, -1, -1):
    if score[i] >= score[i+1]:
        minus = score[i] - score[i+1] + 1
        score[i] -= minus
        count += minus
print(count)
