# 회의실 배정
import sys

n = int(sys.stdin.readline())
meetings = []
count = 1 # 첫번째 회의는 무조건 선택

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))

meetings.sort(key=lambda x : (x[1], x[0])) # 끝나는 시간을 기준으로 정렬(핵심)
end = meetings[0][1] # 첫번째 회의의 끝나는 시간
for i in range(1, n):
    if meetings[i][0] >= end:
        end = meetings[i][1] # i번째 회의의 끝나는 시간
        count += 1

print(count)
