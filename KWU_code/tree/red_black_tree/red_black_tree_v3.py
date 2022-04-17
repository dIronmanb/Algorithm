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

class Red_Black_Tree():
    def __init__(self):
        self.NULL = Node(0, None)
        self.NULL.color = 0
        self.root = self.NULL
    
    def search(self, key):
        return self.search_tree_helper(self.root, key)
    
    def search_tree_helper(self, node, key):
        if node is None or node.key == key:
            return node # 해당하는 key를 찾게 되면 반환
        
        if key < node.key:
            return self.search_tree_helper(node.left, key)
        
        else:
            return self.search_tree_helper(node.right, key)

    def RIGHT_ROTATE(self, X):
        
        print("(RIGHT ROTATE)")
        
        Y = X.left
        
        X.left = Y.right
        if Y.right != None:
            Y.right.parent = X
        Y.parent = X.parent
        if X.parent == None:
            self.root = Y   
        elif X == X.parent.right:
            X.parent.right = Y
        else:
            X.parent.left = Y
        Y.right = X
        X.parent = Y

    def LEFT_ROTATE(self, X): 
        
        print("(LEFT ROTATE)")
        
        Y = X.right
        X.right = Y.left
        if Y.left != None:
            Y.left.parent = X
        
        Y.parent = X.parent
        if X.parent == None:
            self.root = Y
        
        elif X == X.parent.left:
            X.parent.left = Y
        else:
            X.parent.right = Y
        Y.left = X
        X.parent = Y
        
    def RB_insert(self, key):  
        N = Node(key, None)
        
        y = None
        x = self.root
        
        while x == None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
                
        N.parent = y
        
        if y == None:
            self.root = N
        elif node.key < y.key:
            y.left = N
        else:
            y.right = N
            
        if N.parent == None:
            N.color = "BLACK"
            return

        if N.parent.parent == None:
            return
            
            
        while N.parent and N.parent.color == "RED":
            if N.parent == N.parent.parent.right:
                U = N.parent.parent.left
                
                if U and U.color == "RED":
                    U.color = "BLACK"
                    N.parent.color = "BLACK"
                    N.parent.parent.color = "RED"
                    N = N.parent.parent
                    
                else:
                    if N == N.parent.left:
                        N = N.parent
                        self.RIGHT_ROTATE(N)
                    N.parent.color = "BLACK"
                    N.parent.parent.color = "RED"
                    self.LEFT_ROTATE(N.parent.parent)
                    
            else:
                
                U = N.parent.parent.right 
                
                if U and U.color == "RED":
                    U.color = "BLACK"
                    N.parent.color = "BLACK"
                    N.parent.parent.color = "RED"
                    N = N.parent.parent
                    
                else:
                    if N == N.parent.right:
                        N = N.parent
                        self.LEFT_ROTATE(N)
                    N.parent.color = "BLACK"
                    N.parent.parent.color = "RED"
                    self.RIGHT_ROTATE(N.parent.parent)
                    
            if N == self.root:
                break
            
        self.root.color = "BLACK"

x = random.sample(range(10),10) # x는 list타입 0~999까지
# x = [9, 13, 10, 1, 6, 10, 7, 8, 4, 2]
value = x[5]

rb_tree = Red_Black_Tree()

n = 1
for i in x:
    print("index {}: {}".format(n, i))
    n += 1
    rb_tree.RB_insert(i)


for i in range(len(x)):
    
    node = rb_tree.search(x[i])
    print(rb_tree.root.key)
    print("find x[{}]: {}, color: {}, parent: {}".format(i, node.key, node.color, node.parent.key if node.parent else "None"))
    print("\tleft: {}, right: {}".format(node.left.key if node.left else "None", node.right.key if node.right else "None"))
    print()
