'''
    Red Black Tree
    - 균형 이진 트리
    - mission: 삽입, 검색 구현
    - furthermore: 삭제까지!
    
   AVL-tree의 base는 그대로 따라감
   균형을 잡기 위한 연산
   - 단일 회전
   - 이중 회전: 한 번 flatten + 단일 회전
   
   삽입 연산
   - case 1: 빈 트리
   - case 2: P가 black
   - case 3: P가 red
   - case 3-1: P가 red, U도 red
   - case 3-2: P가 red, U가 black
   
'''
import random

class Node:
    
    def __init__(self, key, parent = None):
        self.key = key
        self.left = None
        self.right = None
        
        # When create node, the color is red
        self.color = "red"
        
        # parent that indicate upper node
        self.parent = parent
def insert(node, key, parent):
    
    # insert(root, key, None)
    if node is None:
        node = Node(key, parent)
        return node
     
    elif key < node.key:
        node.left = insert(node.left, key, node)
        
    else:
        node.right = insert(node.right, key, node)
        
    # root는 계속 받을 수 있게끔 node 반환
    return node
def search(node, value):
    
    # 처음 시작은 root
    # 점점 아래로 deeper    
    if node is None or node.key == value:
        return node 
    
    if value < node.key: 
        return search(node.left, value)
    
    else:
        return search(node.right, value)

# RB tree balancing operation
def right_rotate(node):
    
    if(node == None or node.left == None):
        return 
    
    L = node.left
    node.left = L.right
    
    if L.right != None:
        
        L.right.parent = node
    
    L.right = node
    L.parent = node.parent
         
    if node == node.parent.right:
        node.parent.right = L
    elif node == node.parent.left:
        node.parent.left = L
    
    else:
        root = L
        
    node.parent = L
    
    
def left_rotate(node):
    
    if(node == None or node.right == None):
        return 
    
    R = node.right
    node.right = R.left

    if R.left != None:
        
        R.left.parent = node
    
    R.left = node
    R.parent = node.parent
    
    
    if node == node.parent.right:
        node.parent.right = R
    elif node == node.parent.left:
        node.parent.left = R
    else:
        root = R
         
    node.parent = R


# get info related with node: 하아....
def get_node_info(node):
    n = node
    p = node.parent
    s = node.parent.right if node.parent.left == node else node.parent.left
    g = p.parent if p is not None else None
    if g:
        u = g.right if g.left == p else g.left
    else:
        u = None
    return n,p,s,g,u


def RB_insert(node, key):
    
    # 결국 root를 반환    
    
    root = insert(node, key, None)
    
    node = search(root, key)
    
    # node가 3개 이상일 때부터 시작
    # OR
    # node, parent, uncle, grandpa가 필요
    
    if node.parent is None or node.parent.parent is None:
        root.color = "black"
        print(root.key, root.color)
        return root
    
    # 노드 5개 총정리
    n, p, s, g, u = get_node_info(node)

        
        
    while (n and p and s and g and u) and node.parent.color == "red":
        if node.parent == node.parent.parent.right:
            uncle = node.parent.parent.left
            
            if uncle.color == "red":
                uncle.color = "black"
                node.parent.color = "black"
                node.parent.parent.color = "red"
                node = node.parent.parent
                
            elif node == node.parent.left:
                node = node.parent
                node_left = right_rotate(root, node)
                if node_left.parent is None:
                    root = node_left
            
            
            node.parent.color = "black"
            node.parent.parent.color = "red"
            node_right = left_rotate(root, node)
            if node_right.parent is None:
                root = node_right
            
        else:
            uncle = node.parent.parent.right
            
            if uncle.color == "red":
                uncle.color = "black"
                node.parent.color = "black"
                node.parent.parent.color = "red"
                node = node.parent.parent
                
            elif node == node.parent.left:
                node = node.parent
                node_left = right_rotate(root, node)
                if node_right.parent is None:
                    root = node_left
                
            node.parent.color = "black"
            node.parent.parent.color = "red"
            node_right = left_rotate(root, node)
            if node_right.parent is None:
                root = node_right
            
            
    root.color = "black"
            
                


if __name__ == "__main__":
    
    x = random.sample(range(1000), 20)
    index = 5
    value = x[index]

    root = None
    
    n = 1
    for i in x:
        print("{} : {}".format(n , i))
        
        n += 1
        RB_insert(root, i)
        print()
        
    # print("(root) key:{} , node.left:{}, node.right:{}, node.color:{}, node.parent:{}".\
    #      format(root.key, root.left, root.right, root.color, root.parent))
    
    print(root)
    
    node = search(root, value)
    print(node.key, node.color)