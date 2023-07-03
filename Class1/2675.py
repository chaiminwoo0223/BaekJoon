'''
# 문자열 반복
t = int(input())
for i in range(t):
    r, s = map(str, input().split())
    r = int(r)
    s = list(s)
    for j in range(len(s)):
        print(s[j]*r, end='')
    print() # 줄넘김
'''
t = int(input())
for i in range(t):
    r, s = map(str, input().split())
    for j in s:
        print(j*int(r), end='')
    print() # 줄넘김