# 부분 문자열
# ValueError -> try-except
import sys

while True:
    try:
        s, t = map(str, sys.stdin.readline().split())
        count = 0
        start = 0

        for i in range(len(s)):
            for j in range(start, len(t)):
                if s[i] == t[j]:
                    start = j + 1
                    count += 1
                    break
                
        if count == len(s):
            print("Yes")
        else:
            print("No")
    except:
        break
