# 스타트와 링크
from itertools import combinations
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
numbers = list(range(n))
difference = 100
combination = list(combinations(numbers, n//2)) # 모든 팀 조합 구하기

def calculator(team):
    score = 0
    for x in team:
        for y in team:
            score += graph[x][y]
    return score

for i in range(len(combination)//2): # 중복 계산 방지
    team1 = combination[i] # 팀1
    team2 = [number for number in numbers if number not in team1] # 팀2
    score1 = calculator(team1) # 팀1 능력치
    score2 = calculator(team2) # 팀2 능력치
    difference = min(difference, abs(score1 - score2)) # 차이

print(difference)
