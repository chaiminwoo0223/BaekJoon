# DNA
import sys

n, m = map(int, sys.stdin.readline().split())
DNA = []
result = ""
number = 0

for _ in range(n):
    DNA.append(sys.stdin.readline().rstrip())

for j in range(m):
    count = [0, 0, 0, 0] # A, C, G, T
    for i in range(n):
        if DNA[i][j] == 'A':
            count[0] += 1
        elif DNA[i][j] == 'C':
            count[1] += 1
        elif DNA[i][j] == 'G':
            count[2] += 1
        else:
            count[3] += 1
    idx = count.index(max(count))
    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'C'
    elif idx == 2:
        result += 'G'
    else:
        result += 'T'
    number += (n - max(count))

print(result)
print(number)
