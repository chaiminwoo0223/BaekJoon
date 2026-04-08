# 웜홀
# 벨만-포드
# 음의 가중치
# 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때, 출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다.
import sys

def bellman_ford(x):
    distances = [0] * (x+1)

    for i in range(x):
        for j in range(1, x+1):
            for next_node, next_distance in graph[j]:
                new_distance = distances[j] + next_distance

                if distances[next_node] > new_distance:
                    distances[next_node] = new_distance

                    if i == x-1: # # n번째에도 값이 줄어든다면, 음의 사이클 존재
                        return True

    return False

input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append([E, T])
        graph[E].append([S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append([E, -T])

    if bellman_ford(N):
        print("YES")
    else:
        print("NO")
