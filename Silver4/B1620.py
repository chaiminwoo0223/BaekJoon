# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline # Customize
n, m = map(int, input().split())
dogam_num = {}
dogam_name = {}

for i in range(1,n+1):
  pokemon = input().rstrip()
  dogam_num[i] = pokemon
  dogam_name[pokemon] = i

for _ in range(m):
  check = input().rstrip()
  if check.isdigit():
    print(dogam_num[int(check)])
  else:
    print(dogam_name[check])