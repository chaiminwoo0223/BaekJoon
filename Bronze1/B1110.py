# 더하기 사이클
import sys

n = sys.stdin.readline().rstrip()
number1 = n
number2 = 0
number3 = 0
count = 0

while True:
    if len(number1) != 1:
        number2 = str(int(number1[0]) + int(number1[1]))
    else:
        number2 = "0" + number1

    number3 = number1[-1] + number2[-1]
    count += 1
    
    if int(number3) != int(n):
        number1 = number3
    else:
        break

print(count)
