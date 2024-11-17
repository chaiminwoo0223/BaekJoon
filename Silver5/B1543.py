# 문서 검색
import sys

document = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
n = len(document)
k = len(word)
start = -1
count = 0

for i in range(n):
    if i >= start:
        if document[i:i+k] == word:
            count += 1
            start = i+k
print(count)
