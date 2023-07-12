# 달팽이는 올라가고 싶다.
import math

a, b, v = map(int, input().split())
cnt = (v-b)/(a-b) # 핵심
print(math.ceil(cnt))