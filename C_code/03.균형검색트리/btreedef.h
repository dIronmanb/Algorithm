#ifndef _BTREE_DEF_
#define _BTREE_DEF_

#define BTREE_ORDER		5


typedef struct BTreeNodeDataType //B-트리 노드 데이터에는 다음과 같은 정보가 있다.
{
	int key;		// 해당 노드의 키 (ex) 가령 내가 원하는 노드를 찾으려 할 때 크기순으로 쪼개고 쪼개지는...
	char value;		// 내가 넣으려는 값(=데이터)
} BTreeNodeData;

typedef struct BTreeNodeType
{
	int                     count;	// 현재 한 B-트리 노드에 데이터가 얼마나 쌓였는지
	BTreeNodeData           data[BTREE_ORDER];	// B-트리 노드 데이터의 개수: m - 1
	struct BTreeNodeType*   children[BTREE_ORDER+1]; // B-트리의 자식 노드를 각각 가리키게 됨: m
} BTreeNode;

#endif
