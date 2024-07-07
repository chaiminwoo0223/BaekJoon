# 진법 변환
import sys

# 입력 받기
n, b = sys.stdin.readline().strip().split()
b = int(b)

# 결과 출력
print(int(n, b))
