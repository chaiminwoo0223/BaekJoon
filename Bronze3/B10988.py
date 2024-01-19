# 팰린드롬인지 확인하기
import sys

word = sys.stdin.readline().strip()

print(1 if word == word[::-1] else 0)