# 회의실 배정
import sys

n = int(sys.stdin.readline())
meetings = []
count = 0

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))

meetings = sorted(meetings, key=lambda x: (x[1], x[0])) # 끝나는 시간을 기준으로 정렬
start = 0
end = 0

for meeting in meetings:
    if meeting[0] >= end:
        start = meeting[0]
        end = meeting[1]
        count += 1

print(count)
