# 탑
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다.
n = int(input())
tower = list(map(int, input().split()))
stack = [0]
result = [0] * n

for i in range(1, n):
    while stack and tower[stack[-1]] <= tower[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1] + 1

    stack.append(i)

print(*result)
