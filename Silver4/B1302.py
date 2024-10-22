# 베스트셀러
from collections import Counter
import sys

n = int(sys.stdin.readline())
book = []

for i in range(n):
    book.append(sys.stdin.readline().rstrip())

book = Counter(sorted(book))
print(book.most_common(1)[0][0])
