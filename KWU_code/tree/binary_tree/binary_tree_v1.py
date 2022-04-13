'''
    이진 트리(binary tree)
    
    - 이진 트리 노드 클래스
        key, left, right, parent, data(현재는 data = key)
        
    - 삽입 insert
    - 검색 search
    - 삭제 delete
    
'''

import random
from timeit import default_timer as timer

# Create Binary Tree Node
class Node:
    
    def __init__(self, data, parent = None):
        self.key = data
        self.left = None
        self.right = None
        
        # node의 부모를 알려주어야 함.
        self.parent = parent
    
# Search value
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
    
# Insert Tree Node
def insert(node, key, parent):
    
    # 현재 node가 아무것도 없다면, 즉 해당 위치가 leaf node가 될 위치면
    # 또는 현재 노드가 없다는 것 root로도 볼 수 있다.
    if node is None:
        
        # Create node
        
        # node.key = key
        # node.left = None
        # node.right = None
        
        # parent는 바로 상단의 node를 의미함.
        node = Node(key, parent)
        return node
     
    # key가 현재 node의 key보다 작으면
    elif key < node.key:
        # node의 left에 insert
        node.left = insert(node.left, key, node)
        
    # key가 현재 node의 key보다 크면
    else:
        # node의 right에 insert
        node.right = insert(node.right, key, node)
        

    #### ??????? ####
    return node

# Delete Node and Return connce
def delete_node(node):
    
    # node가 leaf node인 경우
    if node.left == None and node.right == None:
        # 이어줄 node가 없으므로 None 반환
        return None
    
    # node.left만 있는 경우
    elif node.left != None and node.right == None:
        
        # node.left에 있는 node를 반환
        return node.left
    
    # node.right만 있는 경우
    elif node.left == None and node.right !=  None:
        
        # node.right에 있는 node를 반환
        return node.right
    
    # 현재 삭제할 node에 자식 노드가 2개인 경우
    else:
        # 현재 node.right를 임시로 담음
        temp = node.right
        
        # 해당 right에서 left만을 바라보며 최솟값 가져오기
        while temp.left != None:
            
            # 현재 node와 (= parent)
            temp_parent = temp
            # 다음 left node 가져오기
            temp = temp.left
        
        
        # 현재 temp는 최솟값을 가진 node이다.
        # node를 삭제하는 것 대신에, node.key에 temp.key(최솟값)을 대입한다.
        node.key = temp.key
        
        # while문을 바로 빠져나온 경우엔
        if temp == node.right:
            #### 바로 right가 temp이니까 ####
            # node를 삭제하는 것 대신에, temp의 값을 가지고온다.
            # key는 이미 위의 코드에서 처리했으므로 right도 가져온다.
            node.right = temp.right
        else:
            #### temp가 2층 이상에서부터 가져왔을 때 ####
            # 현재 temp를 가져왔기 때문에 temp의 parent는 끊어져 있다.
            # 이를 해결하기 위해 temp의 parent의 left엔, temp.right를 이어준다.
            temp_parent.left = temp.right
        
        # tip!
        # 현재 삭제할 노드의 left는 전혀 신경쓰지 않았다.
        # 이는 삭제할 노드를 정말 삭제한 게 아니라 삭제 노드의 right만 잘 수정하여 
        # deleted node를 갱신한 것이다.
        # 따라서, deleted node의 left는 그대로 보존될 것이다.
        return node

# Delete Tree Node
def delete(root, key):
    
    # 해당 key의 node가 있는지부터 확인
    check_node = search(root, key)
    
    # 해당 key의 node가 존재한다면 
    if check_node:
        
        left_node = delete_node(check_node)

        # 아무 노드도 없다면
        if not left_node:
            pass
        
        # 삭제할 노드의 부모 노드가 left가 삭제할 노드면
        if check_node.parent.left == check_node:
            # 삭제 노드 부모의 left에 끊어진 트리를 이어주기
            check_node.parent.left = left_node            
         
        # 삭제할 노드의 부모 노드가 right가 삭제할 노드면
        if check_node.parent.right == check_node:
            # 삭제 노드 부모의 left에 끊어진 트리를 이어주기
            check_node.parent.right = left_node
        
        # 삭제할 노드가 루트라면
        else:
            # left_node가 트리가 된다.
            root = left_node  
            
            
    
    # 해당 key의 node가 없다면
    else:
        print("This binary Tree dosen't have your input value!")
        
# main
if __name__ == "__main__":

    x = random.sample(range(5000), 1000)
    index = 100
    value = x[index]


    root = None
    for i in x:
        # 현재 root만 집어넣고, 다시 출력으로 root를 꺼낸다.
        # root에서부터 시작해야 하므로!
        # 단점: balanced binary tree를 기대할 수 없다.
        root = insert(root, i, None)
        
        
    start = timer()
    found = search(root, value)

    print("\nPresent x[{}] value: {}".format(index, value))
    print(timer() - start)

    if found is not None:
        print('value: ', value, "\nfound: ", found.key, sep = "")
        print("True" if found.key == value else "False")
        

    print("\nDelete x[{}] value {}".format(index, value))

    # Delete Value
    delete(root, value)
    found = search(root, value)
    print(found)

    # Delete Value: 이때는 에러발생이 정상
    delete(root, value)



    
    
    