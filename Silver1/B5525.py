# IOIOI
# 문자열 연산
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
i = 0
count = 0
result = 0

while i < m-1:
    if s[i:i+3] == "IOI":
        count += 1
        i += 2
        if count == n:
            result += 1
            count -= 1
    else:
        count = 0
        i += 1
print(result)
