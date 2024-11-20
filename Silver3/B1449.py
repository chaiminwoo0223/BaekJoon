# 수리공 항승
import sys

n, l = map(int, sys.stdin.readline().split())
pipes = sorted(map(int, sys.stdin.readline().split()))
start = pipes[0] # 테이프를 처음 붙이는 시작 지점
count = 1 # 필요한 테이프 개수

for pipe in pipes[1:]:
    if pipe in range(start, start+l): # if (pipe + 0.5) - (start - 0.5) <= l:
        continue
    else:
        start = pipe
        count += 1

print(count)
