MAX_SIZE = 100

memory = [0 for _ in range(MAX_SIZE)]

def fibonacci(num):
    
    memory[0], memory[1] = 1, 1
    
    for i in range(2,num):
        memory[i] = memory[i-1] + memory[i-2]        
        # print(memory)
        # 메모리에 연이어 저장되는 것을 확인할 수 있다.
    
    return memory[num - 1]
    


num = int(input("Input the number of fibonacci >> "))
result = fibonacci(num)

print("Fibonacci of {} is {}".format(num, result))