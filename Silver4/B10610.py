# 30
# 정렬
# 30의 배수는 3의 배수이면서 일의 자리가 0인 수
import sys

n = sorted(sys.stdin.readline().rstrip(), reverse=True)

if '0' in n and sum(map(int, n)) % 3 == 0:
    print("".join(n))
else:
    print(-1)
