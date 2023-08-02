# solved.ac
import sys
def round2(num): # 사사오입
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    cut = round2(n*0.15)
    score = [int(sys.stdin.readline()) for _ in range(n)]
    score.sort()
    rst = score[cut:n-cut] # 범위를 정확하게 잡아라!
    print(round2(sum(rst)/len(rst)))