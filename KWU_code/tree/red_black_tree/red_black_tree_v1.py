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
from timeit import default_timer as timer

class Node:
    
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        
        # When create node, the color is red
        self.color = "red"
        
        # parent that indicate upper node
        self.parent = parent
        
        
def right_rotate(root, node):
    # node: right rotate의 주축이 되는 node를 의미
    
    # node의 왼쪽 자식 노드를 가져옴
    L = node.left
    
    # node의 왼쪽에는 L의 right를 연결함.
    node.left = L.right
    
    # L.right가 아무것도 없는 게 아니라면
    if L.right != None:
        
        # L.right.parent는 node가 될 것이다.
        # node와 L.right 간의 부모자식 관계를 확실시한다.
        L.right.parent = node
        
    # node가 root면
    if node.parent == None:
        # L을 root로 갱신
        root = L
        
    # node의 부모의 오른쪽 자식이 node면
    elif node == node.parent.right:
        # 오른쪽 자식인 node를 L로 대체
        node.parent.right = L
    # node의 부모의 왼쪽 자식이 node면
    else:
        # 왼쪽 자식인 node를 L로 대체
        node.parent.left = L
    
    # 이제 L.right엔 회전된 node를 연결한다.
    L.right = node
    
    # 이떄 node의 parent는 L이 된다.
    node.parent = L
    
    
def left_rotate(root, node):
    # right의 반대로 코드를 작성하면 된다.
    
    R = node.right
    node.right = R.left
    if R.left != None:
        R.left.parent = node
    if node.parent == None:
        root = R
    elif node == node.parent.right:
        node.parent.right = R
    else:
        node.parent.left = R
    R.left = node
    node.parent = R 
    

def BT_insert(node, key, parent):
    
    if node is None:
        # leaf 노드 생성
        node = Node(key, parent)
        return node
     
    # key가 현재 node의 key보다 작으면
    elif key < node.key:
        # node의 left에 insert
        node.left = BT_insert(node.left, key, node)
        return node.left
        
    # key가 현재 node의 key보다 크면
    else:
        # node의 right에 insert
        node.right = BT_insert(node.right, key, node)
        return node.right
    
def search(node, value):
    
    # 해당 key가 있는 node가 없거나 혹은 있는 경우
    if node is None or node.key == value:
        # None OR Node 반환
        return node 
    
    # 내가 찾으려는 value가 현재 node의 key값보다 작은 경우
    if value < node.key: 
        # node의 왼쪽으로 이동
        return search(node.left, value)
    
    # 내가 찾으려는 value가 현재 node의 key값보다 큰 경우
    else:
        # node의 오른쪽으로 이동
        return search(node.right, value)
    
    
def RB_insert(root, key):
    
    
    node = BT_insert(root, key, None)
            
    print("node.key: {} , node.color: {}, node.parent: {}".format(node.key, node.color, node.parent.key if node.parent else node.parent))
    
    if node.parent and node.parent.parent:
        
        # node.parent의 color가 red인 경우는 계속 loop 
        while node.parent and node.parent.color == "red":
            
            # parent가 오른쪽 자식이라면
            if node.parent == node.parent.right:
                
                # 왼쪽엔 uncle이 존재한다.
                uncle = node.parent.parent.left
                
                # case 3-1
                # P.color == red, U.color == red, Of course N.color == red
                if uncle.color == "red":
                    uncle.color = "black"
                    node.parent.color = "black"
                    # uncle과 parent가 모두 black이 되면서 높이가 1이 증가했으므로
                    node.parent.parent.color = "red"
                    
                    # node의 Grandpa까지 올라가서 해당 Grandpa node에서는 
                    # red black rule를 지키도록 계속 loop -> 다만 black엔 문제가 없으므로 red에 한해서만 loop를 돈다
                    node = node.parent.parent
                    
                # U.color == black, P.color == red, N.color == red
                # 이때, node가 부모의 왼쪽 자식이라면
                elif node == node.parent.left:
                    node = node.parent
                    # 한 번 right rotate
                    right_rotate(root, node)
                
                # 먼저 parent는 black으로, grandpa는 red로 바꿈
                node.parent.color = "black"
                node.parent.parent.color = "red"
                # node.Grandpa에 대해 left_rotate 실행
                left_rotate(root, node.parent.parent) 
                
            # parent가 왼쪽 자식이라면...위의 흐름도와 똑같이 진행하되 반대로
            else:
                
                
                uncle = node.parent.parent.right
                
                if uncle.color == "red":
                    uncle.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                    
                elif node == node.parent.left:
                    node = node.parent
                    right_rotate(root, node)
                    
                    
                # print("node.key: {} , node.color: {}, node.parent: {}".format(node.key, node.color, node.parent.key if node.parent else node.parent))    
                
                if node.parent is not None:
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    left_rotate(root, node.parent.parent)
                
        root.color = "black"
        
    return node
    
    

if __name__ == "__main__":
    
    x = random.sample(range(100), 10)
    index = 5
    value = x[index]

    root = None
    
    n = 1
    for i in x:
        print("{} : {}".format(n , i))
        
        n += 1
        # 현재 root만 집어넣고, 다시 출력으로 root를 꺼낸다.
        # root에서부터 시작해야 하므로!
        # 단점: balanced binary tree를 기대할 수 없다.
        root = RB_insert(root, i)
        print()
        
        
    start = timer()
    found = search(root, value)

    print("\nPresent x[{}] value: {}".format(index, value))
    print(timer() - start)
    print()
    
    if found is not None:
        print('value: ', value, "\nfound: ", found.key, sep = "")
        print("True" if found.key == value else "False")
    else:
        print("found is None")
        
            
            

    
    