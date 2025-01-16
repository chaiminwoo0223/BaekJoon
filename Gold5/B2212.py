# 센서
# 영역
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
censor = sorted(map(int, sys.stdin.readline().split()))
length = sorted((censor[i+1] - censor[i]) for i in range(n-1))

print(sum(length[:n-k]))
