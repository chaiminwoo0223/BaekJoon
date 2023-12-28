# 알파벳 찾기
from string import ascii_lowercase

s = input()
alpha_list = list(ascii_lowercase)
for i in ascii_lowercase:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')