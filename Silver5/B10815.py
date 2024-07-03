# 숫자 카드
import sys

n = int(sys.stdin.readline().strip())
cards = set(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
queries = list(map(int, sys.stdin.readline().strip().split()))

# 결과를 저장할 리스트
result = []

# queries의 각 요소가 cards에 있는지 확인하고 결과 저장
for query in queries:
    if query in cards:
        result.append('1')
    else:
        result.append('0')

# 결과를 한 줄로 출력
print(' '.join(result))
