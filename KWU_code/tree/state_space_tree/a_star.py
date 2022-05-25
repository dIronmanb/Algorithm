import heapq

class Queue(object):
    
    def __init__(self):
        self.elements = []
        
    def __len__(self):
        return len(self.elements)
    
    def push(self, x, priority):
        heapq.heappush(self.elements, (priority, x))
        
    def pop(self):
        return heapq.heappop(self.elements)[1]
    
    
grid = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
         [ 0, 3, 0, 0, 0, 0, 2, 0, 1, 0 ],
         [ 0, 3, 1, 1, 1, 0, 1, 0, 1, 0 ],
         [ 0, 0, 1, 0, 1, 0, 1, 1, 1, 0 ],
         [ 0, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ]

start = (1, 5)
goal = (8, 1)


queue = Queue()
queue.push(start, 0)
came_from = {}
cost_so_far = {}
cost_so_far[start] = 0

def _calc_cost(current, next):
    (x,y) = next
    return cost_so_far[current] + grid[y][x]

def heuristic(goal, next):
    (x1, y1) = goal
    (x2, y2) = next
    dx = x1 - x2
    dy = y1 - y2
    return dx * dx + dy * dy


while len(queue) > 0:
    current = queue.pop()
    
    if current == goal:
        break
    
    (x,y) = current
    candidates = [(x + 1, y), (x, y-1), (x-1,y), (x, y+1)]
    for next in [(h, v) for h,v in candidates if grid[v][h] != 0]:
        new_cost = _calc_cost(current, next)
        if next not in came_from or new_cost < cost_so_far[next]:
            queue.push(next, new_cost + heuristic(goal, next))
            cost_so_far[next] = new_cost
            came_from[next] = current
            
current = goal
path = []
while current is not start:
    path.append(current)
    current = came_from[current]
path.reverse()
print(path)
    

