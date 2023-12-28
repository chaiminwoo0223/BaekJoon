# 단어 공부
from string import ascii_uppercase

word = input().upper()
alpha_list = list(ascii_uppercase)
max = 0
for i in ascii_uppercase:
    if max < word.count(i):
        max = word.count(i)
        result = i
    elif max == word.count(i):
        result = '?'
print(result)
