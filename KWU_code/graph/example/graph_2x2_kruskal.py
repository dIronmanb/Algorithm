import graphviz

g = graphviz.Graph(format = 'png', filename = "graph_kruskal", directory = "visulization")
g.attr(rankdir = 'LR', size = '10.0')

def get_parent(parent, x):
    
    # single node with no connection 
    if parent[x] == x:
        return x
    # otherwise, call my parent node recursively
    parent[x] = get_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    
    # connect smaller ones
    if a < b:
        parent[b] = a
    else:
        parent[a] = b    
def find_parent(parent, a, b):

    a = get_parent(parent, a)
    b = get_parent(parent, b)
    
    if a == b:
        return 1
    else:
        return 0   
    

# definite edge class 
class Edge():
    
    def __init__(self, a, b, cost):
        self.node = [a,b]
        self.cost = cost
        
# make empty list called "road"
road = []
   
# deinfite node num and edge num
n = 7
m = 12       
      
# add edge
road.append(Edge(1, 2, 3))
road.append(Edge(1, 3, 2))
road.append(Edge(3, 2, 1))
road.append(Edge(2, 5, 2))
road.append(Edge(3, 4, 4))
road.append(Edge(7, 3, 6))
road.append(Edge(5, 1, 5))
road.append(Edge(1, 6, 2))
road.append(Edge(6, 4, 1))
road.append(Edge(6, 5, 3))
road.append(Edge(4, 5, 3))
road.append(Edge(6, 7, 4))

# sort by cost of edge
road.sort(key = lambda x : x.cost)

# save where the graph contains each node
parent =  [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
    
sum = 0
edge_num = 0
new_graph = []
for i in range(len(road)):
    
    # if there is no cycle
    if not find_parent(parent, road[i].node[0], road[i].node[1]):
        sum += road[i].cost
        edge_num += 1
        new_graph.append(road[i])
        union_parent(parent, road[i].node[0], road[i].node[1])

    if edge_num == n - 1:
        break

print(sum)
for i in new_graph:
    print(i.node, i.cost)
    
    g.node(str(i.node[0]))
    g.node(str(i.node[1]))
    g.edge(str(i.node[0]), str(i.node[1]), label = str(i.cost))
    
g.render(view = False)

    
