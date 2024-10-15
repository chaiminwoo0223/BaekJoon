# 셀프 넘버
# 속도: 리스트 <<< 집합
def d(number):
    result = number
    for j in str(number):
        result += int(j)
    return result

numbers = set(range(1, 10000))
results = set()

for number in numbers:
    results.add(d(number))

# 셀프 넘버
for number in sorted(numbers-results):
    print(number)
