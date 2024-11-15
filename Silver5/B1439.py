# 뒤집기
import sys

s = sys.stdin.readline().rstrip()
zero = 0
one = 0
now = -1

for i in range(len(s)):
    if s[i] != now:
        now = s[i]
        if now == "0":
            zero += 1
        else:
            one += 1
print(min(zero, one))
