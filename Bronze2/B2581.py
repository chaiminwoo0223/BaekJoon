# 소수
import sys

# 입력 받기
m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
decimal = []

# m 이상 n 이하 자연수 중 소수
for i in range(m,n+1):
        for j in range(2,i+1):
            if i % j == 0:
                if i == j:
                    decimal.append(i)
                break

# 결과 출력
if len(decimal):
    print(sum(decimal))
    print(min(decimal))
else:
    print(-1)
