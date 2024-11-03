# 잃어버린 괄호
import sys

s = sys.stdin.readline().rstrip().split("-")
result = []

for number in s[0].split("+"):
    result.append(int(number))

for numbers in s[1:]:
    for number in numbers.split("+"):
        result.append(-int(number))

print(sum(result))
