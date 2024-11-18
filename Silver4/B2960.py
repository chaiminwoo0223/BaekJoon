# 에라토스테네스의 체
import sys

n, k = map(int, sys.stdin.readline().split())
numbers = list(range(2, n+1))
find_number = 0
count = 0

while find_number == 0:
    remove_number = []
    number = min(numbers) # 소수
    
    for i in range(len(numbers)):
        if numbers[i] % number == 0:
            remove_number.append(numbers[i])
    
    for r in remove_number:
        numbers.remove(r)
        count += 1
        if count == k:
            find_number = r
            print(r)
