# from copyreg import constructor
# from turtle import fillcolor
import graphviz

# # dot = graphviz.Digraph('round-table', comment = 'The Round Table')
# dot = graphviz.Graph(format = 'png'
#                      )
# dot.node('A', 'King Arthur')  
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')
# print(dot.source)

# dot.render(directory = 'temp_graph').replace('\\', '/')
# dot.render(directory='doctest-output', view=True) 



# 방향이 있는 노드를 사용
# 일단 서버에서 노드간의 이미지를 바로 볼 수 있도록 png파일로 저장
g = graphviz.Digraph(format = 'png')

g.node('Red', style = 'filled', fillcolor = 'red2')
g.node('Black', style = 'filled', fillcolor = 'gray38')

g.edge('Red', 'Black')

print(g.source)

g.render(directory = 'temp_graph').replace('\\', '/')
