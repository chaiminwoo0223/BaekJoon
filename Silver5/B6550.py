# 부분 문자열
# 포함 + 순서
# 무한루프 방지
import sys

while True:
    try:
        s, t = map(str, sys.stdin.readline().split())
        s = list(map(str, s))
        index = 0

        for i in range(len(t)):
            if index < len(s):
                if s[index] == t[i]:
                    index += 1
            else:
                break

        if index == len(s):
            print("Yes")
        else:
            print("No")
    except:
        break
