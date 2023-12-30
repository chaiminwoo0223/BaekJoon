# 팩토리얼 0의 개수
import math
n = int(input())
num = list(str(math.factorial(n)))
cnt = 0

for i in num[::-1]: # 핵심
    if i != '0':
        break
    else:
        cnt += 1
print(cnt)
