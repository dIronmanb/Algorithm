# import graphviz
from collections import deque

# make Graph
# g = graphviz.Digraph(format = 'png', filename = "graph", directory = "visulization")
# g.attr(rankdir = "LR")

# 어떤 구조로 그래프를 만들 것인가??
# 무향그래프이므로 2 x 2 matrix는 비효율적
# 현재 노드 이름이 숫자 아님
# (결론) 연결 리스트로 그래프 표현

graph = {}

# 냄비에 물 붓기
graph["pour water into a pot"] = ["ignition"]

# 점화
graph["ignition"] = ["add ramen", "add ramen soup", "add eggs"]

# 라면 넣기
graph["add ramen"] = ["add eggs"]

# 계란 넣기
graph["add eggs"] = []

# 라면 봉지 뜯기
graph["open a bag of ramen"] = ["add ramen", "add ramen soup"]

# 라면 수프 넣기
graph["add ramen soup"] = ["add eggs"]


# for key, value in graph.items():
    
#     g.node(key)
    
#     for i in value:
#         g.node(i)
#         g.edge(key, i)
    
# g.render(view = False)    

# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - #
# algorthm # 

# depth first search
def dfs(g, node):
    visited[node] = True
    
    for i in g[node]:
        if visited[i] == False:
            dfs(g, i)
    sequence.appendleft(node)

# make linked list
sequence = deque()

# make "visited" memory
visited = {key : False for key in graph.keys()}

# topological sort
for key, value in graph.items():
    
    for i in value:
        if visited[key] == False:
            dfs(graph, key)
            
for i in sequence:
    print(i)