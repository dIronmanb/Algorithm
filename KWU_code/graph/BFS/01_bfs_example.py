from collections import deque

class Queue(object):
    
    def __init__(self):
        self.elements =  deque()
        
    def __len__(self):
        return len(self.elements)
    
    def push(self, x):
        self.elements.append(x)
        
    def pop(self):
        return self.elements.popleft()
    
    

grid = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
         [ 0, 1, 0, 0, 0, 0, 1, 0, 1, 0 ],
         [ 0, 1, 1, 1, 1, 0, 1, 0, 1, 0 ],
         [ 0, 0, 1, 0, 1, 0, 1, 1, 1, 0 ],
         [ 0, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ]

start = (1 ,5)
goal =  (8, 1)


queue = Queue() # queue
queue.push(start)
came_from = {} # memory

while len(queue) > 0:
    current = queue.pop()
    
    if current == goal:
        break
    
    
    (x, y) = current
    
    candidates = [(x + 1, y),  (x, y - 1), (x - 1, y), (x, y + 1)]
    for next in [(h,v) for h,v in candidates if grid[v][h] != 0]: # 후보군 안에서 BFS 계속 진행
        if next not in came_from:
            queue.push(next)
            came_from[next] = current
            
current = goal
path = []
while current is not start:
    path.append(current)
    current = came_from[current]
    
path.reverse()
print(path)
