# 카드 정렬하기
# 가장 작은 묶음 2개를 찾아서 더하는 것이 가장 적게 비교하는 방법
import sys
import heapq

n = int(sys.stdin.readline())
cards = []
result = 0

for i in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

while len(cards) > 1:
    number1 = heapq.heappop(cards)
    number2 = heapq.heappop(cards)
    sum_number = number1 + number2
    result += sum_number
    heapq.heappush(cards, sum_number)

print(result)
