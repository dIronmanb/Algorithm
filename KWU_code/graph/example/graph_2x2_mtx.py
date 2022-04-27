import graphviz

# make Graph
g = graphviz.Graph(format = 'png', filename = "graph", directory = "visulization")
g.attr(rankdir = 'LR', size = '10.0')
graph = [   [1, 2, 3],
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


for i in graph:
    g.node(str(i[0]))
    g.node(str(i[1]))
    g.edge(str(i[0]), str(i[1]), label = str(i[2]))
    
     
#     g.node(key)
    
#     for i in value:
#         g.node(i)
#         g.edge(key, i)
    
g.render(view = False)    

