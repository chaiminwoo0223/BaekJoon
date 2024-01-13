# 분수찾기
import sys

num = int(sys.stdin.readline())
line = 1

while num > line: # 지그재그
    num -= line
    line += 1

if line % 2 == 0:
    a = num
    b = line - num + 1
else:
    a = line - num + 1
    b = num
print(f'{a}/{b}')