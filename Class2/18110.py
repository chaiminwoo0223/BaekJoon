# solved.ac
import sys
def round2(num): # 사사오입
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    ban = round2(n*0.15)
    score = [int(sys.stdin.readline()) for _ in range(n)]
    score.sort()
    rst = 0
    for i in range(ban, n-ban): # sum()를 사용하지 않고 계산을 진행해야 한다!
        rst += score[i]
    rst = rst/(n-2*ban)
    print(round2(rst))