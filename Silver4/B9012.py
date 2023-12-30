# 괄호
t = int(input())

for i in range(t):
    PS = input()
    while "()" in PS:
        PS = PS.replace("()", "") # 핵심
    if len(PS) == 0:
        print("YES")
    else:
        print("NO")