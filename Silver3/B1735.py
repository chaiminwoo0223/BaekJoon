# 분수 합
from fractions import Fraction
import sys

a, b = map(int, sys.stdin.readline().strip().split())
c, d = map(int, sys.stdin.readline().strip().split())

numerator = a * d + c * b # 분자
denominator = b * d # 분모
result = Fraction(numerator, denominator) # 기약분수

print(result.numerator, result.denominator)
