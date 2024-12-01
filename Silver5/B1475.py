# 방 번호
import sys

n = sys.stdin.readline().rstrip()
counter = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
count = 0

for i in n:
    number = int(i)
    if number in (6, 9):
        if counter[6] == counter[9]:
            counter[6] += 1
        else:
            counter[9] += 1
    else:
        counter[number] += 1

for c in counter:
    if counter[c] > count:
        count = counter[c]
print(count)
