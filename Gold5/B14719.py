# 빗물
import sys

h, w = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split())) # 각 열의 블록 높이
result = 0 # 고인 물의 총량

# 각 열에서 물이 고일 수 있는 양 계산
for i in range(1, w-1): # 맨 왼쪽과 맨 오른쪽은 물이 고이지 않음
    left = max(heights[:i]) # 현재 열 왼쪽에서 가장 높은 블록
    right = max(heights[i+1:]) # 현재 열 오른쪽에서 가장 높은 블록
    water = min(left, right) # 현재 열에 고일 수 있는 최대 높이

    if water > heights[i]: # 블록이 물 보다 낮을 때만 물이 고일 수 있음
        result += water - heights[i]

print(result)
