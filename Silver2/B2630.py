# 색종이 만들기
# 정사각형 모양의 종이
# 분할 정복 : 재귀적으로 자신을 호출하면서, 그 연산의 단위를 조금씩 줄여가는 방식
import sys

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [0, 0]

def check(x, y, n):
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                check(x, y, n // 2)
                check(x, y + n // 2, n // 2)
                check(x + n // 2, y, n // 2)
                check(x + n // 2, y + n // 2, n // 2)
                return # 핵심: 함수 종료
            
    result[color] += 1 # 핵심2


check(0, 0, n)
print(result[0])
print(result[1])
