'''
    Challenge
    1. 그대로
    2. 오름차순을 내림차순으로
    3. 오른쪽부터 정렬이 아닌 왼쪽부터 정렬
'''

import random
from timeit import default_timer as timer


# 선택 정렬

# 0. 데이터를 무작위로 mixed
# 1. 가장 큰 값을 찾아서 -> 맨 오른쪽에 두기
# 2. 그 다음 큰 값을 찾아서 -> 맨 오른쪽에 두기

def selection_sort(data):
    
    # From last index To second index(first index는 이미 하나이므로 정렬이 된 것이다.)
    for i in range(len(data) - 1, 0, -1):
        # 현재 index "i"에는 가장 큰 값이 있다고 가정
        largest = i
         
        for j in range(i): 
            if data[largest] > data[j]:
                largest = j
             
        data[largest], data[i] = data[i], data[largest]
        

def test(data):
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            return False
    return True

data = random.sample(range(20), 10)
start = timer()
selection_sort(data)

print("Running Time:", timer() - start)
print("data[0:10]:", data[0:10])
print("Test Result:", test(data))