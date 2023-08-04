# 통계학
import sys
from collections import Counter
def ISmode(x):
    cnt = Counter(x).most_common()
    if len(cnt)>1 and cnt[0][1]==cnt[1][1]: # 최빈값 2개 이상
        return cnt[1][0]
    else:
        return cnt[0][0]

n = int(sys.stdin.readline())
num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
print(round(sum(num)/len(num))) # 산술평균
print(num[n//2]) # 중앙값
print(ISmode(num)) # 최빈값***
print(num[-1]-num[0]) # 범위