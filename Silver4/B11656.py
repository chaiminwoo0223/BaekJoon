# 접미사 배열
import sys

input = sys.stdin.readline

s = input().rstrip()
x = [s[i:] for i in range(len(s))]

for a in sorted(x):
    print(a)
