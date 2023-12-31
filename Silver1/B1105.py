# 팔
import sys

l, r = sys.stdin.readline().split()
cnt = 0

if len(l) != len(r):
    print(0)
else:
    for i in range(len(r)):
        if l[i] == r[i]:
            if l[i] == '8':
                cnt += 1
        else:
            break # 핵심
    print(cnt)