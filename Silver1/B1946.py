# 신입 사원
# 그리디 알고리즘, 정렬
# 순위
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = []

    for _ in range(n):
        a, b = map(int, input().split())
        result.append([a, b])

    result = sorted(result, key=lambda x: x[0]) # 서류심사 성적
    cnt = 1
    x = result[0][1]

    for i in range(1, n): # 면접 성적
        if x > result[i][1]:
            cnt += 1
            x = result[i][1]

    print(cnt)
