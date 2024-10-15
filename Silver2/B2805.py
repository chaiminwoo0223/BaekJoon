# 나무 자르기
import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start = 0 # 시작점
end = max(trees) # 끝점
result = 0

while start <= end:
    mid = (start + end) // 2 # 중간점
    total = 0

    # 현재 중간 높이로 나무를 잘랐을 때, 얻을 수 있는 나무의 길이 총합
    for tree in trees:
        if tree > mid:
            total += (tree - mid)

    # 이분 탐색
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
    
print(end) # 절단기에 설정할 수 있는 높이의 최댓값
