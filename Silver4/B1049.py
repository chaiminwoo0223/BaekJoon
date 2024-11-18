# 기타줄
import sys

n, m = map(int, sys.stdin.readline().split())
package = []
single = []
result = 0

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    package.append(x)
    single.append(y)

min_package = min(package)
while n > 0:
    if n >= 6:
        min_single = min(single) * 6
        n -= 6
    else:
        min_single = min(single) * n
        n -= n

    if min_package > min_single:
        result += min_single
    else:
        result += min_package

print(result)
