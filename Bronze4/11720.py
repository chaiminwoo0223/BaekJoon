# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
n = int(input())
num = input()
sum = 0

for i in range(n):
    sum += int(num[i])
print(sum)