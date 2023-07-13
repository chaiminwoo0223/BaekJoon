# Hashing
# ord(문자): 문자에 해당하는 유니코드 숫자 값을 반환
l = int(input())
word = input()
result = 0

for i in range(l):
    result += (ord(word[i])-96)*(31**i) # 핵심
print(result % 1234567891)