# 쇠막대기
# + 1
import sys

input = sys.stdin.readline()

x = input.rstrip()
cnt = 0
stack = []

for i in range(len(x)):
    if x[i] == '(': # 쇠막대기 추가
        stack.append(x[i])
    else:
        stack.pop()

        if x[i-1] == '(': # 레이저
            cnt += len(stack)
        else: # 쇠막대기 끝 (중요)
            cnt += 1

print(cnt)
