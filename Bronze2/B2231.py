# 분해합
# sum(list)
n = int(input())

for i in range(1,n+1):
    num = list(map(int, str(i))) # 분해
    result = sum(num) + i # 분해합
    if result == n:
        print(i)
        break
    elif i == n:
        print(0)
