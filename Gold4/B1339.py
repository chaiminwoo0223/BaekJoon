# 단어 수학
from collections import Counter
import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for i in range(n)]
dictionary = Counter()
number = 9
result = 0

# 각 알파벳의 계수 계산
for word in words:
    for i, c in enumerate(word):
        if c not in dictionary:
            dictionary[c] = 10**(len(word)-i-1)
        else:
            dictionary[c] += 10**(len(word)-i-1)

for value in sorted(dictionary.values(), reverse=True): # 계수 기준으로 내림차순 정렬
    result += value * number # 계수 * 가장 큰 숫자 할당
    number -= 1 # 가장 큰 숫자 감소

print(result)
