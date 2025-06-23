# 생일
# students.append([name, int(day), int(month), int(year)]) # 리스트 추가
# students.sort(key=lambda x: (x[3], x[2], x[1])) # 년, 월, 일 순으로 정렬
n = int(input())
students = []

for i in range(n):
    name, day, month, year = input().split()
    students.append([int(year), int(month), int(day), name]) # [년, 월, 일, 이름]

students.sort() # 오름차순 정렬

print(students[-1][3]) # 가장 나이가 적은 사람
print(students[0][3]) # 가장 나이가 많은 사람
