# 차집합
# 리스트 << 집합
import sys

a, b = map(int, sys.stdin.readline().split())
number1 = set(map(int, sys.stdin.readline().split()))
number2 = set(map(int, sys.stdin.readline().split()))
result = sorted(number1 - number2)

print(len(result))
print(*result) # join 보다 더 좋음
