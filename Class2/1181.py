# 단어 정렬
n = int(input())
result = []
num = 1
for i in range(n):
    word = input()
    result.append(word)

result = list(set(result)) # 중복 제거
result = sorted(result) # 알파벳 순으로 정렬
result.sort(key=len) # 길이 순으로 정렬
for j in result:
    print(j)