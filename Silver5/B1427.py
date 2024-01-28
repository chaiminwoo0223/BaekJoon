# 소트인사이드
import sys

number = sys.stdin.readline().rstrip()
reversed_number = sorted(number, reverse=True)

print(''.join(reversed_number))