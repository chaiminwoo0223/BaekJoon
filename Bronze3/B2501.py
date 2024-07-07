# 약수 구하기
import sys

# 입력 받기
n, k = map(int, sys.stdin.readline().strip().split())
measure = []

# 약수
for i in range(1, n+1):
    num = n % i
    if num == 0:
        measure.append(i)

# 결과 출력
if len(measure) < k:
    print(0)
else:
    print(measure[k-1])
