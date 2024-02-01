# 킹, 퀸, 룩, 비숍, 나이트, 폰
import sys

chess_pieces = [1, 1, 2, 2, 2, 8]
current_pieces = list(map(int, sys.stdin.readline().rstrip().split()))
difference = [standard - current for standard, current in zip(chess_pieces, current_pieces)]

print(' '.join(map(str, difference)))