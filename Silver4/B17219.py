# 비밀번호 찾기
import sys

dictionary = dict()

n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    key, value = map(str, sys.stdin.readline().split())
    dictionary[key] = value

for _ in range(m):
    key = sys.stdin.readline().rstrip()
    if key in dictionary:
        print(dictionary.get(key))
