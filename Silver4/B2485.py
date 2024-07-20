# 가로수
from math import gcd
import sys

# 입력 받기
n = int(sys.stdin.readline().strip())
colonnade = [int(sys.stdin.readline().strip()) for _ in range(n)]
count = 0

# 리스트 간격 계산
intervals = [colonnade[i] - colonnade[i-1] for i in range(1, n)]

# 모든 간격의 최대 공약수
gcd_value = intervals[0]
for interval in intervals[1:]:
    gcd_value = gcd(gcd_value, interval)

# 추가할 가로수
for interval in intervals:
    count += ((interval//gcd_value) - 1)

# 결과 출력
print(count)
