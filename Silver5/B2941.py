# 크로아티아 알파벳
import sys

word = sys.stdin.readline().rstrip()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for croatian in croatia:
    word = word.replace(croatian, '*')
print(len(word))