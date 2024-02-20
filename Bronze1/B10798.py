# 세로읽기
import sys

words = []
vertical_string = ''

for _ in range(5):
    words.append(sys.stdin.readline().rstrip())

length = max(len(word) for word in words)

for i in range(length):
    for j in range(5):
        if i < len(words[j]):
            vertical_string += words[j][i]  # 문자를 바로 문자열에 추가

print(vertical_string)