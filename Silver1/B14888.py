# 연산자 끼워넣기
# 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split())) # 수열
plus, minus, multiply, divide = map(int, sys.stdin.readline().split()) # 연산자
maximum = -1e9 # 최댓값 초기화
minimum = 1e9 # 최솟값 초기화

def dfs(depth, number, plus, minus, multiply, divide):
    global maximum, minimum

    if depth == n:
        maximum = max(number, maximum)
        minimum = min(number, minimum)
        return
    
    if plus > 0:
        dfs(depth + 1, number + numbers[depth], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(depth + 1, number - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(depth + 1, number * numbers[depth], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(depth + 1, int(number / numbers[depth]), plus, minus, multiply, divide - 1) # 나눗셈은 정수 나눗셈으로 몫만 취함

dfs(1, numbers[0], plus, minus, multiply, divide)

print(maximum)
print(minimum)
