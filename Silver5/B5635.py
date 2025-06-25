students = []

for i in range(int(input())):
    name, day, month, year = input().split()
    students.append([int(year), int(month), int(day), name])

students.sort()
print(students[-1][-1]) # 가장 나이가 적은 사람
print(students[0][-1]) # 가장 나이가 많은 사람
