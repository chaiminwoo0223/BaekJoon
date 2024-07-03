# 문자열 집합
import sys

# 입력받기
n, m = map(int, sys.stdin.readline().strip().split())

# 문자열 집합 S와 결과 카운트 초기화
strings = set()
count = 0

# 집합 S에 문자열 추가
for _ in range(n):
    strings.add(sys.stdin.readline().strip())

# 검사할 문자열이 집합 S에 있는지 확인
for _ in range(m):
    query = sys.stdin.readline().strip()
    if query in strings:
        count += 1

# 결과 출력
print(count)
