'''
 1. red black tree 구현
 2. ...
 3. ...
 
 흐음... solution보면서 고칠 부분 고치기!

'''


import random

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
    
    print("(RIGHT ROTATE)")
    # print("(RIGHT ROTATE!) X.key: {}, X.left.key: {}".format(X.key, X.left.key if X.left else "None"))
    
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
    
    print("(LEFT ROTATE)")
    # print("(LEFT ROTATE!) X.key: {}, X.right.key: {}".format(X.key, X.right.key if X.right else "None"))
      
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
    
    if N and N.parent == None:
        N.color = "BLACK"
        return N
    
    if N.parent and N.parent.parent == None: 
        N.parent = "BLACK"
        return N.parent
          
         
    while N.parent and N.parent.color == 'RED':

        if N.parent == N.parent.parent.right:
            U = N.parent.parent.left
            
            # Case 3-2
            if U == None or U.color == "BLACK":
                                    
                if N.parent.parent.right == N.parent:
                    
                    # Case 3-2-2
                    if N.parent.left == N:
                        N.color = "BLACK"
                        N.parent.parent.color = "RED"
                        
                        root_ = RIGHT_ROTATE(N.parent)
                        if root_:
                            root = root_
                            
                        # 만약 현재 Node가 3개인 상황이라면 -> root와 같이 있다면
                        if N.parent == root:
                            root_ = LEFT_ROTATE(N.parent)
                        # Node가 4개 이상이라면
                        else:                        
                            root_ = LEFT_ROTATE(N.parent.parent)
                        if root_:
                            root = root_    
                        
                            
                    # Case 3-2-1                          
                    elif N.parent.right == N:

                        N.parent.color = "BLACK"
                        N.parent.parent.color = "RED"
                        root_ = LEFT_ROTATE(N.parent.parent)
                        if root_:
                            root = root_
                        
                        
                
                elif N.parent.parent.left == N.parent:
                    
                    # Case 3-2-4
                    if N.parent.right == N:
                        N.color = "BLACK"
                        N.parent.parent = "RED" 
                        
                        root_ = LEFT_ROTATE(N.parent)
                        if root_:
                            root = root_
                        root_ = RIGHT_ROTATE(N.parent.parent)
                        if root_:
                            root = root_
                        
                    
                    # Case 3-2-3
                    elif N.parent.left == N:
                        N.parent.color = "BLACK"
                        N.parent.parent.color = "RED"
                        root_ = RIGHT_ROTATE(N.parent.parent)
                        if root_:
                            root = root_
            
            # Case 3-1                    
            elif U.color == 'RED':
                N.parent.color = "BLACK"
                U.color = 'BLACK'
                N.parent.parent.color = 'RED'
                # 상단 G node로 이동
                N = N.parent.parent
                
# - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # -
        elif N.parent == N.parent.parent.left:
            
            U = N.parent.parent.right
            
            # Case 3-2
            if U == None or U.color == "BLACK":
                
                if N.parent.parent.left == N.parent:
                    
                    # Case 3-2-2
                    if N.parent.right == N:
                        N.color = "BLACK"
                        N.parent.parent.color = "RED"
                        
                        root_ = LEFT_ROTATE(N.parent)
                        if root_:
                            root = root_
                            
                        # 만약 현재 Node가 3개인 상황이라면 -> root와 같이 있다면
                        if N.parent == root:
                            root_ = RIGHT_ROTATE(N.parent)
                        # Node가 4개 이상이라면
                        else:
                            root_ = RIGHT_ROTATE(N.parent.parent)
                        if root_:
                            root = root_    
                        
                                                
                        
                    # Case 3-2-1                          
                    elif N.parent.left == N:

                        N.parent.color = "BLACK"
                        N.parent.parent.color = "RED"
                        root_ = RIGHT_ROTATE(N.parent.parent)
                        if root_:
                            root = root_
                        
                        
                
                elif N.parent.parent.right == N.parent:
                    
                    # Case 3-2-4
                    if N.parent.left == N:
                        N.color = "BLACK"
                        N.parent.parent = "RED" 
                        
                        root_ = RIGHT_ROTATE(N.parent)
                        if root_:
                            root = root_
                        root_ = LEFT_ROTATE(N.parent.parent)
                        if root_:
                            root = root_
                        
                    
                    # Case 3-2-3
                    elif N.parent.right == N:
                        N.parent.color = "BLACK"
                        N.parent.parent.color = "RED"
                        root_ = LEFT_ROTATE(N.parent.parent)
                        if root_:
                            root = root_
            
            # Case 3-1                    
            elif U.color == 'RED':
                N.parent.color = "BLACK"
                U.color = 'BLACK'
                N.parent.parent.color = 'RED'  
                N = N.parent.parent              
                
            
    root.color = 'BLACK'        
    return root

x = random.sample(range(10),10) # x는 list타입 0~999까지
# x = [9, 13, 10, 1, 6, 10, 7, 8, 4, 2]
value = x[5]

root = None
n = 1
for i in x:
    print("index {}: {}".format(n, i))
    n += 1
    root = RB_insert(root, i)


for i in range(len(x)):
    
    node = search(root, x[i])
    print("find x[{}]: {}, color: {}, parent: {}".format(i, node.key, node.color, node.parent.key if node.parent else "None"))
    print("\tleft: {}, right: {}".format(node.left.key if node.left else "None", node.right.key if node.right else "None"))
    print()
