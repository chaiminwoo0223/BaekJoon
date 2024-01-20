# 1로 만들기
import sys

n = int(sys.stdin.readline())
cnt = [0] * (n+1) # 숫자 i를 1로 만들 때 필요한 최소 연산 횟수를 저장하는 배열

for i in range(2,n+1):
    cnt[i] = cnt[i-1] + 1
    if i % 2 == 0:
        cnt[i] = min(cnt[i], cnt[i//2] + 1)
    if i % 3 == 0:
        cnt[i] = min(cnt[i], cnt[i//3] + 1)

print(cnt[n])