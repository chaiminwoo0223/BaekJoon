# 폴리오미노
import sys

board = sys.stdin.readline().rstrip()
result = ""

i = 0
while len(board) > i:
    if board[i:i+4] == "XXXX":
        result += "AAAA"
        i += 4
    elif board[i:i+2] == "XX":
        result += "BB"
        i += 2
    elif board[i] == ".":
        result += "."
        i += 1
    else:
        result = ""
        break

if result:
    print(result)
else:
    print(-1)
