# 한수
import sys

x = int(sys.stdin.readline())
count = 0

for i in range(1, x+1):
    if i < 100:
        count += 1
    else:
        str_num = str(i)
        interval = int(str_num[0]) - int(str_num[1])
        for j in range(1, len(str_num)-1):
            if (int(str_num[j]) - int(str_num[j+1])) == interval:
                count += 1
            else:
                break

print(count)
