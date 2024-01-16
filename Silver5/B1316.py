# 그룹 단어 체커
import sys

n = int(sys.stdin.readline())
cnt = n

for _ in range(n):
    words = sys.stdin.readline()
    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            pass
        elif words[i] in words[i+1:]:
            cnt -= 1
            break
print(cnt)      