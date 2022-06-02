import random
from timeit import default_timer as timer


# def insert_sort(data):
    
#     for i in range(1, len(data)):    
#         temp = data[i]
#         prev = i - 1
        
#         while(prev >= 0) and (data[prev] > temp):
#             data[prev + 1] = data[prev]
#             prev -= 1
#         data[prev + 1] = temp
        
# def shell_sort(data, h):

#     # data를 h개 만큼 나누기
#     '''
#     h = 3
#     1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    
#     1     4     7     10       13
#       2     5     8      11       14
#         3     6     9       12       15
    
#     ''' 
#     splited_data = [[] for i in range(h)]
    
#     for j in range(h):
#         for i in count(i, h):
#             splited_data[j].append(data[i])
        
    
    



h_list = [57, 23, 10, 4, 1]  
    
def shell_sort(data):
    
    N = len(data)
    
    for h in h_list:
        for i in range(h, N):
            temp = data[i]
            j = i - h
            while j >= 0 and data[j] > temp:
                data[j + h] = data[j]
                j -= h
            data[j + h] = temp
        

def test(data):
    for i in range(1, len(data)):
        if data[i - 1] > data[i]:
            return False
    return True

data = random.sample(range(10000), 100)

start = timer()
shell_sort(data)


print(data[:30])
print("Is data sorted?? ", test(data))
print("Running Time: {}".format(timer() - start))