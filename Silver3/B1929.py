# 소수 구하기
# 핵심: 문제풀이 시, 알고리즘 분류를 반드시 확인하자!
def ISprime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1): # 에라토스테네스의 체
            if num % i == 0:
                return False
        return True

n, m = map(int, input().split())
for j in range(n, m+1):
    if ISprime(j):
        print(j)