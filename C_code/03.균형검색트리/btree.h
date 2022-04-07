#ifndef _B_TREE_
#define _B_TREE_

#include "btreedef.h"
#include "btlinkedstack.h"

typedef struct BTreeType
{
	BTreeNode *pRootNode;   //루트 노드
} BTree;

// B-트리 생성.
BTree* createBTree();

// B-트리 삭제.
void deleteBTree(BTree* pBTree);

// 검색.
BTreeNodeData* searchBT(BTree* pBTree, int key);

// 자료 추가.
int addDataBT(BTree* pBTree, BTreeNodeData data);

// 자료 제거.
int removeDataBT(BTree* pBTree, int key);

// B-트리 표시.
void displayBTree(BTree *pTree);


// 그외 내부 함수들.
BTreeNode* createBTreeNode(BTreeNodeData data);

void addNodeBT(BTreeNode* pCurrentNode,
				BTreeNodeData data,
				BTreeNode* pRChildNode);

// 노드 분리
void splitNodeBT(BTree* pBTree, LinkedStack* pStack);

// 말단 노드인가?
int isLeafNode(BTreeNode* pParentNode);

// 말단 노드 교환
BTreeNode* replaceLeafNodeBT(BTree *pBTree, BTreeNode* pDelNode, int index,
                LinkedStack* pStack);

// 노드 제거
void deleteBTreeNode(BTreeNode* pBTreeNode);

// key 제거...?
void deleteKeyBT(BTreeNode* pNode, int index);

// B-트리의 균형 유지
void balanceBTree(BTree* pBTree, LinkedStack* pStack);

// 인덱스 추출...?
int getIndexInfo(BTreeNode* pParentNode, BTreeNode* pCurrentNode);

// 오른쪽 노드를 빌려옴
void borrowRightNodeBT(BTreeNode* pParentNode, BTreeNode* pCurrentNode,
                int index, BTreeNode* pRightNode);

// 왼쪽 노드를 빌려옴
void borrowLeftNodeBT(BTreeNode* pParentNode, BTreeNode* pCurrentNode,
                int index, BTreeNode* pLeftNode);

// 노드 합병
void mergeNodeBT(BTree *pBTree, LinkedStack* pStack, BTreeNode* pParentBTreeNode,
                BTreeNode* pCurrentBTreeNode, int index);

void displayBTreeNode(BTreeNode *pNode);

#endif

