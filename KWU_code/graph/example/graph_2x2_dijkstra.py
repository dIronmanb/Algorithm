import graphviz

# make Graph
g = graphviz.Graph(format = 'png', filename = "graph_dijkstra", directory = "visulization")
g.attr(rankdir = 'LR', size = '10.0')
info = [   [1, 2, 3],
            [1, 3, 2],
            [3, 2, 1],
            [2, 5, 2],
            [3, 4, 4],
            [7, 3, 6],
            [5, 1, 5],
            [1, 6, 2],
            [6, 4, 1],
            [6, 5, 3],
            [4, 5, 3],
            [6, 7, 4]  ]

INF = int(1e9)
n = 7
m = 12

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for i in range(m):
    start, end, cost = info[i]
    graph[start].append((end,cost))
    graph[end].append((start,cost))
    
def get_smallest_node():
    min_value = INF
    index = 0
    
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
            
    return index


def dijkstra(start):
    
    distance[start] = 0
    visited[start] = True
    
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    for _ in range(n - 1):
        
        next = get_smallest_node()
        visited[next] = True
        
        for j in graph[next]:
            cost = distance[next] + j[1]
            
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                # 더 먼 거리는 어떻게 삭제할까?
                try:
                    graph[start].remove(j)
                    graph[j[0]].remove((start, j[1])) # 이게 맞나?
                except:
                    pass
                             
                
for start in range(1, n + 1):
    dijkstra(start)
    print("start node: {} >> {}".format(start, distance))
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)
    
    
# make graph
'''
g =
 [
     [(1,2), (4,5), ...],
     [(0, 10), (4, 1), ...],
     .
     .
     .
 ]

'''
for i in range(1, n):
    
    g.node(str(i))
    
    for j in graph[i]:
        g.node(str(j[0]))
        g.edge(str(i), str(j[0]), label = str(j[1]))
        
g.render(view = False)
    

    
       
    
    
    