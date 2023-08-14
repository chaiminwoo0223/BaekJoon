# 집합
# 핵심1: sys.stdin.readline().split() --> [' ', ' ', ... , ' ']
# 핵심2: len(['all']) == 1
import sys
m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    x = sys.stdin.readline().split()
    if len(x) == 1:
        if 'all' in x:
            S = set(range(1,21))
        elif 'empty' in x:
            S = set()
    else:
        command, target = x[0], int(x[1])
        if command == 'add':
            S.add(target)
        elif command == 'remove':
            S.discard(target)
        elif command == 'check':
            if target in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if target in S:
                S.discard(target)
            else:
                S.add(target)