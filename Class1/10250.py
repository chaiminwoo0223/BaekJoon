# ACM 호텔
# 층과방
# //(몫)
t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n%h
    num = n//h + 1
    if n%h == 0:
        floor = h
        num = n//h
    print(floor*100 + num)