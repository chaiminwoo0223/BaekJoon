# 카드 합체 놀이
# 우선순위 큐: 가장 큰 값 또는 가장 작은 값을 구할 때 매우 유용함
import sys
import heapq 

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
heapq.heapify(numbers)

for _ in range(m):
    number1 = heapq.heappop(numbers)
    number2 = heapq.heappop(numbers)
    number3 = number1 + number2
    heapq.heappush(numbers, number3)
    heapq.heappush(numbers, number3)

print(sum(numbers))
