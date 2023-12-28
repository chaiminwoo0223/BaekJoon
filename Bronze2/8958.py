# OX퀴즈
n = int(input())

for i in range(n):
    count = 0
    sum = 0
    str = input()
    for j in str:
        if j =='O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)