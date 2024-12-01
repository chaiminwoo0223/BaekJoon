# 셀프 넘버
numbers = list(range(1, 10001))
result = set()

for number in numbers:
    for i in str(number):
        number += int(i)
    if number not in result and number <= 10000:
        result.add(number)

for r in sorted(set(numbers) - result):
    print(r)
