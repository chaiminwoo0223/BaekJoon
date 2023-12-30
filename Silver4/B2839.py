# 설탕 배달
n = int(input())
cnt = 0

while n >= 0:
    if n % 5 == 0:
        cnt += (n // 5)
        print(cnt)
        break
    else:
        n -= 3
        cnt += 1
else: # 핵심: else는 If문 뿐만 아니라, While문에서도 사용할 수 있다!
    print(-1)