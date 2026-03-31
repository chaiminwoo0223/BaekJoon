# 암호 만들기
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다
# 정렬된 문자열을 선호 -> 알파벳이 암호에서 증가하는 순서로 배열
from  itertools import combinations
import sys

input = sys.stdin.readline

l, c = map(int, input().split())
x = list(map(str, input().split()))
s = {'a', 'e', 'i', 'o', 'u'}
m = s - (s - set(x)) # 모음
n = set(x) - s # 자음

result = []

for i in range(1, len(m)+1):
    codes = []

    for combination1 in combinations(m, i):
        codes = [*combination1]

        if l - i < 2:
            break

        for combination2 in combinations(n, l-i):
            result.append("".join(sorted(codes + [*combination2])))

for a in sorted(result):
    print(a)
