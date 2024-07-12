# 대칭 차집합
import sys

# 입력 받기
a, b = map(int, sys.stdin.readline().strip().split())
A = set(map(int, sys.stdin.readline().strip().split()))
B = set(map(int, sys.stdin.readline().strip().split()))

# 결과 출력
print(len(A ^ B))
