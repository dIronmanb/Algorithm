import random
from timeit import default_timer as timer

# 버블 정렬
# 특징: 정렬된 데이터에 대해선 O(n)의 시간을 가진다.
# 다만 그게 아니라면 O(n^2)의 시간복잡도를 가진다.

# 구현
# 두 장씩 비교하면서 큰 것을 오른쪽으로 swap
# tip! 이미 정렬된 배열이라면 break!

def bubble_sort(data):
    
    
    for j in range(len(data), 0, -1):
        flag = True
                
        for i in range(1, j):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
                flag = False
        if flag:
             break



def test(data):
    for i in range(1, len(data)):
        if data[i - 1] > data[i]:
            return False
    return True

data = random.sample(range(10000), 100)
start = timer()
bubble_sort(data)

print("Running Time:", timer() - start)
print("data[0:10]:", data[0:10])
print("Test Result:", test(data))