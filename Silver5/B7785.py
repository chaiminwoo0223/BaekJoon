# 회사에 있는 사람
import sys

# 입력 받기
n = int(sys.stdin.readline().strip())
result = set()

# 명령어 처리
for _ in range(n):
    name, cmd = sys.stdin.readline().strip().split()
    
    if (cmd == "enter"):
        result.add(name)
    elif (cmd == "leave"):
        result.remove(name)

# 결과 출력
for name in sorted(result, reverse=True):
    print(name)
