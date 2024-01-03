# 문자열
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline().strip() # 개행 문자 제거
    print(string[0] + string[-1])