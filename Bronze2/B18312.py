# 시각
import sys

n, k = sys.stdin.readline().split()
hour = list(range(int(n)+1))
minute = list(range(60))
second = list(range(60))
hours = []
minutes = []
seconds = []
count = 0

for h in hour:
    if len(str(h)) == 1:
        hours.append("0"+ str(h))
    else:
        hours.append(str(h))

for m in minute:
    if len(str(m)) == 1:
        minutes.append("0"+ str(m))
    else:
        minutes.append(str(m))

for s in second:
    if len(str(s)) == 1:
        seconds.append("0"+ str(s))
    else:
        seconds.append(str(s))

for h in hours:
    for m in minutes:
        for s in seconds:
            if k in h or k in m or k in s:
                count += 1
                
print(count)
