# 행복 유치원
# 그리디 알고리즘
# 차이의 개수는 N-1개이고 여기서 K-1개를 제외 -> (N-1) + (K-1) = N-K
# 각 조에는 원생이 적어도 한 명 있어야 하며, 같은 조에 속한 원생들은 서로 인접해 있어야 한다.
# 조마다 티셔츠를 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다.
# 최대한 비용을 아끼고 싶어 하는 태양이는 K개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고 싶어한다.
n, k = map(int, input().split())
children = list(map(int, input().split()))
cost = sorted([children[i+1] - children[i] for i in range(n-1)])

print(sum(cost[:n-k]))
