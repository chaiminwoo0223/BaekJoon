# 신입 사원
# 성적의 순위
# 그리디 알고리즘
# 정렬
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    result = []

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        result.append([a, b])

    result = sorted(result, key=lambda x: x[0]) # 핵심
    cnt = 1 # 무조건 1명은 뽑는다.
    t = result[0][1]

    for i in range(1, n):
        if result[i][1] < t:
            t = result[i][1]
            cnt += 1

    print(cnt)
