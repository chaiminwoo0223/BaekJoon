# 음계
symphony = list(map(int, input().split()))

if symphony == sorted(symphony):
    print("ascending")
elif symphony == sorted(symphony, reverse=True):
    print("descending")
else:
    print("mixed")
