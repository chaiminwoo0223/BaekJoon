# 로프
# 사용하지 않는 로프가 있을 수 있음
import sys

n = int(sys.stdin.readline())
weights = sorted(list(int(sys.stdin.readline()) for _ in range(n)), reverse=True)
result = []

for i in range(n):
    result.append(weights[i] * (i+1))

print(max(result))
