# 최소공배수
from math import lcm
import sys

a, b = map(int, sys.stdin.readline().strip().split())
print(lcm(a, b))
