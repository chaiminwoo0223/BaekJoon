# 다이얼
import sys

words = sys.stdin.readline().rstrip()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for word in words:
    for idx, group in enumerate(dial):
        if word in group:
            result += idx + 3
            break

print(result)