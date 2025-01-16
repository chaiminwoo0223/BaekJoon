# 이중 우선순위 큐
# 동기화 2번
# 두 힙은 동일한 값을 관리하지만, 서로 독립적인 데이터 구조로 동작
import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    heap_min = [] # 최소힙
    heap_max = [] # 최대힙
    valid = {} # 유효성 검사(삽입된 값과 삭제된 값 관리)

    for _ in range(int(sys.stdin.readline())):
        command, number = sys.stdin.readline().split()
        number = int(number)

        if command[0] == 'I': # 삽입 연산
            heapq.heappush(heap_min, number)
            heapq.heappush(heap_max, -number)
            valid[number] = valid.get(number, 0) + 1 # 삽입된 값의 유효성을 증가
        else: # 삭제 연산
            if number == -1:
                while heap_min and valid.get(heap_min[0], 0) == 0:
                    heapq.heappop(heap_min) # 유효하지 않은 값은 제거
                if heap_min: # 유효한 값이 있으면 삭제
                    x = heapq.heappop(heap_min) # 최솟값 제거
                    valid[x] -= 1 # 해당 값의 유효성을 감소
            if number == 1:
                while heap_max and valid.get(-heap_max[0], 0) == 0:
                    heapq.heappop(heap_max) # 유효하지 않은 값은 제거
                if heap_max: # 유효한 값이 있으면 삭제
                    x = -heapq.heappop(heap_max) # 최댓값 제거
                    valid[x] -= 1 # 해당 값의 유효성을 감소
        
        # 동기화
        while heap_min and valid.get(heap_min[0], 0) == 0:
            heapq.heappop(heap_min) # 유효하지 않은 값은 제거
        while heap_max and valid.get(-heap_max[0], 0) == 0:
            heapq.heappop(heap_max) # 유효하지 않은 값은 제거
        
    if heap_min and heap_max:
        print(-heap_max[0], heap_min[0])
    else:
        print("EMPTY")
