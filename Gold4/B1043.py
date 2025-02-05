# 거짓말
# bfs -> 2중 for문
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
people = list(map(int, sys.stdin.readline().split()))[1:] # 진실을 아는 사람들
visited = [0] * (n+1)
parties = [list(map(int, sys.stdin.readline().split()))[1:] for i in range(m)] # 파티 정보 입력
q = deque()
count = 0

# 진실을 아는 사람은 방문 처리
for person in people:
    q.append(person)
    visited[person] = 1

def bfs():
    while q:
        person = q.popleft()

        for party in parties:
            if person in party: # 진실을 아는 사람이 파티에 포함되면
                for participant in party: # 핵심: 참가자를 탐색
                    if visited[participant] == 0:
                        q.append(participant)
                        visited[participant] = 1

bfs()

for party in parties:
    liar = True # 거짓말 가능 여부

    for participant in party:
        if visited[participant] == 1: # 진실을 아는 사람이 있다면
            liar = False
            break # 더 이상 확인할 필요가 없음

    if liar:
        count += 1

print(count)
