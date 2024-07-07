# 약수들의 합
import sys

while True:
    n = int(sys.stdin.readline().strip())
    measure = []

    if n == -1:
        break

    # 약수
    for i in range(1, n):
        if n % i == 0:
            measure.append(i)
    
    # 결과 출력
    if n == sum(measure):
        measure_str = ' + '.join(map(str, measure))
        print(f"{n} = {measure_str}")
    else:
        print(f"{n} is NOT perfect.")
