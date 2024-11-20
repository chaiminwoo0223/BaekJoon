# 팰린드롬 만들기
from collections import Counter
import sys

name = sorted(map(str, sys.stdin.readline().rstrip()))
counter = Counter(name)
odd = 0 # 핵심
odd_word = "" # 핵심
result = ""

for key in counter: # Key
    if counter[key] % 2 != 0:
        odd += 1
        odd_word += key
    for _ in range(counter[key] // 2):
        result += key

if odd > 1: # 문자의 개수가 홀수인 것이 2개 이상 존재하면, 팰린드롬을 만들 수 없다. 
    print("I'm Sorry Hansoo")
elif odd == 1: # 문자의 개수가 홀수인 것이 1개라면, 팰린드롬을 만들 수 있다.
    print(result + odd_word + result[::-1]) 
else:
    print(result + result[::-1])
