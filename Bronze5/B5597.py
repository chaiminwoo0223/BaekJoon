# 과제 안 내신 분..?
import sys

arr = list(range(1, 31))

for _ in range(28):
    arr.remove(int(sys.stdin.readline()))

for i in range(2):
    print(arr[i])