import random
from timeit import default_timer as timer


# 이진 탐색 구현하기
def binary_search(data, value):
    # 1. sort된 데이터가 있다.
    # 2. 절반씩 나누어서 찾는다.
    # 3. if data[mid] == value: return mid
    #    elif data[mid] < value: 
    #       end = mid - 1, mid  = (start + end)//2
    #    elif data[mid] > value:
    #       start = mid + 1, mid = (start + end)//2
    #
    #
    #
    start = 0
    end = len(data) - 1
    
    mid = (start + end)//2
    
        
    while(1):
        
        if data[mid] == value:
            return mid
    
        elif data[mid] > value:
            end = mid - 1
            mid = (start + end)//2
        else:
            start = mid + 1
            mid = (start + end)//2
            
        if start == end:
            return -1
    

x = random.sample(range(5000), 1000)
x.sort()

value = x[100]
# value = 440

start = timer()
index = binary_search(x, value)


print("time: {}".format(timer() - start))
print('value: ', value, ', found: ', index, sep = '')
print(1 if index >= 0 and x [index] == value else 0)
