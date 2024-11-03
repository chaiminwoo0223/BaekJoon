# 패션왕 신해빈
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    clothes = {}
    for _ in range(int(sys.stdin.readline())):
        item, category = map(str, sys.stdin.readline().split())
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    
    count = 1
    for category in clothes:
        count *= (clothes[category] + 1) # 알몸도 옷이라고 생각함

    print(count - 1) # 아무것도 선택하지 않는 경우 제거
