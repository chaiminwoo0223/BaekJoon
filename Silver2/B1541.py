# 잃어버린 괄호
import sys

s = sys.stdin.readline().rstrip().split("-")
result = []

for i in s[0].split("+"):
    result.append(int(i))
for i in s[1:]: 
    for j in i.split("+"):
        result.append(-int(j))

print(sum(result))
