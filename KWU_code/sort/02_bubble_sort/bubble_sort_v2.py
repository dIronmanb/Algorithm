'''
    Challenge!
    
    왼쪽부터 bubble sort 진행하기!
'''

import random
from timeit import default_timer as timer

def bubble_sort(data):
    
    
    for j in range(len(data)):
        # print(data)
        flag = True
                
        for i in range(len(data) - 1, j, -1):
            
            # left < right이면
            # (오름차순 기준) 서로 swap하기
            if data[i] < data[i - 1]:
                data[i - 1], data[i] = data[i], data[i - 1]
                flag = False
        if flag:
             break



def test(data):
    for i in range(1, len(data)):
        if data[i - 1] > data[i]:
            return False
    return True

data = random.sample(range(20), 10)
start = timer()
bubble_sort(data)

print("Running Time:", timer() - start)
print("data[0:10]:", data[0:10])
print("Test Result:", test(data))