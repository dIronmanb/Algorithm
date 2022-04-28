import graphviz

g = graphviz.Graph(format = 'png', filename = "fruit_graph", directory = "visulization")
g.attr(rankdir = 'LR', size = '10.0')


def get_parent(parent, node):
    if parent[node] == node:
        return node
    parent[node] = get_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, a, b):
    
    a_parent = get_parent(parent, a)
    b_parent = get_parent(parent, b)
    
    if a_parent[0] < b_parent[0]:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent
              
def find_parent(parent, a, b):
    
    if(get_parent(parent, a) == get_parent(parent, b)):
        return 1
    else:
        return 0

class Edge():
    
    def __init__(self, a, b, cost):
        self.node = [a,b]
        self.cost = cost
    
graph = {
    "apple" : "apple", 
    "grape" : "grape",
    "lemon" : "lemon",
    "peer"  : "peer",
    "pineapple" : "pineapple",
    "tomato" : "tomato",
    "corn" : "corn",
    "orange" : "orange",
    "melon" : "melon"
}

fruit_correlation = []

# union_parent(graph, "apple", "grape")
# union_parent(graph, "lemon", "peer")
# union_parent(graph, "pineapple", "apple")
# union_parent(graph, "tomato", "lemon")
# union_parent(graph, "corn", "grape")
# union_parent(graph, "peer", "corn")
# union_parent(graph, "orange", "pineapple")
# union_parent(graph, "lemon", "orange")
# union_parent(graph, "melon", "apple")
# union_parent(graph, "tomato" , "melon")

fruit_correlation.append(Edge("apple", "grape", 5))
fruit_correlation.append(Edge("lemon", "peer", 3))
fruit_correlation.append(Edge("pineapple", "apple", 1))
fruit_correlation.append(Edge("tomato", "lemon", 7))
fruit_correlation.append(Edge("corn", "grape", 10))
fruit_correlation.append(Edge("peer", "corn", 11))
fruit_correlation.append(Edge("orange", "pineapple",2))
fruit_correlation.append(Edge("lemon", "orange",1))
fruit_correlation.append(Edge("melon", "apple", 4))
fruit_correlation.append(Edge("tomato" , "melon", 12))


for i in fruit_correlation:
    
    g.node(i.node[0])
    g.node(i.node[1])
    g.edge(i.node[0], i.node[1], label = str(i.cost))
    
g.render(view = False)
