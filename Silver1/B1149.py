# RGB거리
# 최솟값을 저장해 나가며, 모든 집을 칠했을 때의 최솟값
import sys

n = int(sys.stdin.readline())
costs = []

for _ in range(n):
    costs.append(list(map(int, sys.stdin.readline().rstrip().split()))) # 2차원 배열

# DP 테이블 초기화
for i in range(1, n):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

print(min(costs[-1]))
