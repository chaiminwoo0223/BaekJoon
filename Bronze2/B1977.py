# 완전제곱수
import sys
import math

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
numbers = []

for i in range(n, m+1):
    number = int(math.sqrt(i))
    if i == number**2:
        numbers.append(i)
        
if numbers:
    print(sum(numbers))
    print(min(numbers))
else:
    print(-1)
