# 곱셈
n  = int(input())
m  = int(input())

print(n*(m%10)) # 일의자리
print(n*(m//10%10)) # 십의자리
print(n*(m//100)) # 백의자리
print(n*m)