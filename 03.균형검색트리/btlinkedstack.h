#ifndef _LINKED_STACK_
#define _LINKED_STACK_


typedef struct LinkedStackNodeType
{
	struct BTreeNodeType* data;		   // B-트리 타입의 데이터를 저장할 그릇
	struct LinkedStackNodeType* pLink; // 자기 자신을 가리키는 포인터 하나
} LinkedStackNode;

typedef struct LinkedStackType
{
	int currentCount;           // 현재 원소의 개수
	LinkedStackNode* pTop;      // Top 노드의 포인터
} LinkedStack;

LinkedStack* createLinkedStack();

int pushLS(LinkedStack* pStack, struct BTreeNodeType* data); //push
LinkedStackNode* popLS(LinkedStack* pStack);	//pop
LinkedStackNode* peekLS(LinkedStack* pStack);	//peek

void deleteLinkedStack(LinkedStack* pStack);	
int isLinkedStackFull(LinkedStack* pStack);  //isFull
int isLinkedStackEmpty(LinkedStack* pStack); //isEmpty

#endif
