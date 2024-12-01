# 30
# 정렬
# 30의 배수는 3의 배수이면서 일의 자리가 0인 수
import sys

n = sys.stdin.readline().rstrip()
numbers = sorted(map(int, n), reverse=True)

if '0' not in n or sum(numbers) % 3 != 0:
    print(-1)
else:
    print("".join(map(str, numbers)))
