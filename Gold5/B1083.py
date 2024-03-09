# 소트
# 자료구조
from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split())) 
s = int(stdin.readline())

for i in range(n):
    if s <= 0:
        break
    else:
        # 탐색: 현재 위치에서 s 범위 내 최대값의 정확한 인덱스 찾기
        max_idx = i + nums[i:min(n, i + s + 1)].index(max(nums[i:min(n, i + s + 1)]))
        # 교환: max_idx에서 i로 교환
        while max_idx > i:
            nums[max_idx], nums[max_idx - 1] = nums[max_idx - 1], nums[max_idx]
            max_idx -= 1
            s -= 1
            if s <= 0: 
                break

print(*nums)