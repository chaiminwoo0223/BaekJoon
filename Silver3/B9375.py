# 패션왕 신해빈
from collections import Counter
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = Counter()
    count = 1

    for _ in range(n):
        item, category = map(str, sys.stdin.readline().split()) # 무조건 item, category를 사용한다고 생각하지마!
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    
    for category in clothes: # Key
        count *= (clothes[category] + 1) # 알몸도 옷
    print(count - 1) # 알몸 제거
