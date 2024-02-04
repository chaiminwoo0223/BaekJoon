# 너의 평점은
import sys

subjects = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
total_point = 0
total_grade = 0

for _ in range(20):
    _, grade, level = sys.stdin.readline().rstrip().split()
    if level != "P":
        total_point += float(grade) * subjects[level]
        total_grade += float(grade)

if total_grade > 0:
    print(total_point / total_grade)
else:
    print(0.0)