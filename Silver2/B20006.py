# 랭킹전 대기열
import sys

input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)

    if not rooms:
        rooms.append([(l, n)])
        continue

    for room in rooms:
        if len(room) == m:
            continue

        if room[0][0] - 10 <= l <= room[0][0] + 10:
            room.append((l, n))
            break
    else:
        rooms.append([(l, n)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    for level, name in sorted(room, key = lambda x : x[1]):
        print(level, name)
