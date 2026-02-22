# 행복 유치원
# 그리디 알고리즘
# 최소 비용 (차이 합)
n, k = map(int, input().split())
children = list(map(int, input().split()))
cost = sorted(children[i+1] - children[i] for i in range(n-1))

print(sum(cost[:n-k]))
