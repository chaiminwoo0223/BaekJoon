# 에디터
import sys

left = list(sys.stdin.readline().rstrip())
right = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().rstrip()
    
    if command[0] == 'L' and left:
        right.append(left.pop())
    if command[0] == 'D' and right:
        left.append(right.pop())
    if command[0] == 'B' and left:
        left.pop()
    if command[0] == 'P':
        left.append(command[-1])

print(''.join(left + right[::-1]))
