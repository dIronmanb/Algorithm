import random
import graphviz

class Node(object):
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.color = 'RED'
        
def insert(node, key, parent):
    if node is None:
        node = Node(key, parent)
        
        return node
    elif key < node.key:
        node.left = insert(node.left, key, node)
        
    elif key > node.key:
        node.right = insert(node.right, key, node)
        
    return node

def search(node, key):
    if node is None or node.key == key:
        return node # 해당하는 key를 찾게 되면 color 반환
    
    if key < node.key:
        return search(node.left, key)
    
    else:
        return search(node.right, key)

def RIGHT_ROTATE(X):
    
    print("(RIGHT ROTATE!) X.key: {}, X.left.key: {}".format(X.key, X.left.key if X.left else "None"))
    
    Y = X.left
    
    X.left = Y.right
    if Y.right != None:
        Y.right.parent = X
    Y.parent = X.parent
    if X.parent == None:
        root = Y # insert에서 이미 root는 찾아짐
        root.color = 'BLACK' # rootf
        root.right = X
        X.parent = root
        return root
    
    
    elif X == X.parent.right:
        X.parent.right = Y
    else:
        X.parent.left = Y
    Y.right = X
    X.parent = Y

def LEFT_ROTATE(X): 
    
    print("(LEFT ROTATE!) X.key: {}, X.right.key: {}".format(X.key, X.right.key if X.right else "None"))
      
    Y = X.right
    X.right = Y.left
    if Y.left != None:
        Y.left.parent = X
    Y.parent = X.parent
    
    # no parent => root 
    if X.parent == None:
        root = Y 
        root.color = "BLACK"
        root.left = X
        X.parent = root
        return root
    
    elif X == X.parent.left:
        X.parent.left = Y
    else:
        X.parent.right = Y
    Y.left = X
    X.parent = Y
    
       
def RB_insert(root, key):
    root = insert(root, key, None) # parent가 None이니까 아무것도 안됨...
    N = search(root, key)
    
                
    while(N.parent and N.parent.color == 'RED'):
        
        if N.parent == N.parent.parent.right:
            U = N.parent.parent.left
            
            # Case 3-1                    
            if U and U.color == 'RED':
                U.color = 'BLACK'
                N.parent.color = 'BLACK'
                N.parent.parent.color = 'RED'
                N = N.parent.parent
            
            # Case 3-2
            else:
                # Case 3-2-2 
                if N == N.parent.left:
                    N = N.parent
                    root_ = RIGHT_ROTATE(N)
                    if root_:
                        root = root_ 
                        
                N.parent.color = "BLACK"
                N.parent.parent.color = "RED"                   
                root_ = LEFT_ROTATE(N.parent.parent)
                if root_:
                    root = root_            
                
# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # -
        else:
                
            U = N.parent.parent.right
            
            # Case 3-1                    
            if U and U.color == 'RED':
                U.color = 'BLACK'
                N.parent.color = "BLACK"
                N.parent.parent.color = 'RED'
                N = N.parent.parent
            
            # Case 3-2
            else:
                # Case 3-2-2 
                if N == N.parent.right:

                    N = N.parent
                    root_ = LEFT_ROTATE(N)
                    if root_:
                        root = root_ 
                        
                N.parent.color = "BLACK"
                N.parent.parent.color = "RED"                   
                root_ = RIGHT_ROTATE(N.parent.parent)
                if root_:
                    root = root_
                            
        if N == root:
            break                
                
            
    root.color = 'BLACK'        
    return root

x = random.sample(range(15), 15) # x는 list타입 0~999까지

value = x[5]

root = None
n = 1
for i in x:
    print("index {}: {}".format(n, i))
    n += 1
    root = RB_insert(root, i)

graph = graphviz.Digraph(format = 'png')


for i in range(len(x)):
    
    node = search(root, x[i])
    
    
    # node    
    if node.color == "RED":
        graph.node(str(node.key), style = 'filled', fillcolor = 'red2')
    else:
        graph.node(str(node.key), style = 'filled', fillcolor = 'gray38')
    
    # node.left
    if node.left != None:
        if node.left.color == "RED":
            graph.node(str(node.left.key), style = 'filled', fillcolor = 'red2')
        else:
            graph.node(str(node.left.key), style = 'filled', fillcolor = 'gray38')
    else:
        graph.node("node_left" + str(i), "None")
        
    # right
    if node.right != None:
        if node.right.color == "RED":
            graph.node(str(node.right.key), style = 'filled', fillcolor = 'red2')
        else:
            graph.node(str(node.right.key), style = 'filled', fillcolor = 'gray38')
    else:
        graph.node("node_right" + str(i), "None")  
        
        
    # edges
    if node.left and node.right:
        graph.edge(str(node.key), str(node.right.key))
        graph.edge(str(node.key), str(node.left.key))
        

    elif node.left:
        graph.edge(str(node.key), "node_right" + str(i))
        graph.edge(str(node.key), str(node.left.key))
            
    
    elif node.right:
        graph.edge(str(node.key), str(node.right.key))
        graph.edge(str(node.key), "node_left" + str(i))
        
    else:
        graph.edge(str(node.key), "node_right" + str(i)) 
        graph.edge(str(node.key), "node_left" + str(i))
        
    
        
    
    print("find x[{}]: {}, color: {}, parent: {}".format(i, node.key, node.color, node.parent.key if node.parent else "None"))
    print("\tleft: {}, right: {}".format(node.left.key if node.left else "None", node.right.key if node.right else "None"))
    print()
    
print(graph.source)
graph.render(directory = 'red_black_tree').replace('\\', '/')
    
    