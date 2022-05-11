import graphviz
from collections import deque

# make Graph
g = graphviz.Digraph(format = 'png', filename = "graph", directory = "visulization")
g1 = graphviz.Digraph(format = 'png', filename = "graph_dijkstra", directory = "visulization")

graph = {}

# nodel cost
graph[0] = [(1, 8), (2, 9), (3, 11)]
graph[1] = [(4, 10)]
graph[2] = [(1,6), (4,1), (3,3)]
graph[3] = [(5,8), (6,8)]
graph[4] = [(7,2)]
graph[5] = [(7,5), (2,12)]
graph[6] = [(5,7)]
graph[7] = [(6,4)]

for from_node, info in graph.items():
    g.node(str(from_node))
    
    for to_node, cost in info:
        g.node(str(to_node))
        g.edge(str(from_node), str(to_node), label = str(cost))

# rank same    
with g.subgraph() as s:
    s.attr(rankdir = 'LR', rank = 'same')
    s.node('0')
    s.node('4')
    
with g.subgraph() as s:
    s.attr(rankdir = 'LR', rank = 'same')
    s.node('3')
    s.node('5')    

    
g.render(view = False)    


# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #
# algorthm # 

'''
    DIJKSTRA(G, r)
        "초기화"
        공집합 S를 생성
        모든 노드에 대해
            거리[노드] = oo로 설정
        시작하려는 노드 r에 대해선 거리[r] = 0
        
        "시작"
        S가 V와 같지 않을 때까지(모든 노드를 다 방문할 때까지)
            노드 u << 거리가 가장 작은 node(맨처음이라면 d[u] = 0인 시작노드가 될 것이다)
            S에 노드 u추가(방문)
            노드 u에 연결된 다른 노드들 v에 대하여
                만약 v가 V - S 인 노드이면서 d[u] + u와 v 사이의 거리 < d[v]이면
                    d[v] << d[u] + w(u,v)
                    prev[v] << u: v와 u를 새롭게 연결(저장)
'''

def dijkstra(graph, start):
    
    # init
    S = set()
    V = set(graph.keys())
    arrow = [None for _ in range(len(graph))]
    dist = [1e9 for _ in range(len(graph))]
    dist[start] = 0
    
    # gogo
    while len(S) != len(graph):
        node = extract_min_node(V-S, dist)
        S.add(node)
        
        for to_node, cost in graph[node]:
            if to_node in (V - S) and dist[node] + cost < dist[to_node]:
                dist[to_node] = dist[node] + cost
                arrow[node] = (to_node, dist[to_node])
    
    return dist, arrow
    
def extract_min_node(s, dist):
    min = 1e9
    for node in s:
        if dist[node] < min:
            min = dist[node]
    return dist.index(min)
            
    
a, b = dijkstra(graph, 0)
print(a)
print(b)

for from_node, info in enumerate(b):
    g1.node(str(from_node))    
    
    if info:
        to_node, cost = info
        g1.node(str(to_node))
        g1.edge(str(from_node), str(to_node), label = str(cost)) 
       
g1.render(view = False)  