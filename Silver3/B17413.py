# 단어 뒤집기 2
import sys

s = list(sys.stdin.readline().rstrip())
tag = False
temp = []
result = []

for c in s:
    if c == "<":
        if temp:
            result.append("".join(reversed(temp)))
            temp = []
        result.append(c)
        tag = True
    elif c == ">":
        result.append(c)
        tag = False
    else:
        if tag:
            result.append(c)
        else:
            if c == " ": # 단어와 단어 사이의 공백 처리
                if len(temp) != 0:
                    result.append("".join(reversed(temp)))
                    temp = []
                result.append(c)
            else:
                temp.append(c)

if temp:
    result.append("".join(reversed(temp)))
    temp = []

print("".join(result))
