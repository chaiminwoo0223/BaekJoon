# 부녀회장이 될테야
t = int(input())

for _ in range(t):
    K = int(input())
    N = int(input())
    P = [i for i in range(1,N+1)] # 0층
    for j in range(K):
        for k in range(1,N):
            P[k] += P[k-1] # 핵심!
    print(P[-1])    