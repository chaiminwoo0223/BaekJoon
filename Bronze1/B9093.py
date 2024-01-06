# 단어 뒤집기
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    arr = sys.stdin.readline().split()
    reversed_arr = [word[::-1] for word in arr]
    print(' '.join(reversed_arr))