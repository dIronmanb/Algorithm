#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "btreedef.h"
#include "btlinkedstack.h"

LinkedStack* createLinkedStack()
{
	LinkedStack *pReturn = NULL;
	pReturn = (LinkedStack *)malloc(sizeof(LinkedStack));	// count, pointer 정보가 담겨져 있음
	if (pReturn != NULL) {
		memset(pReturn, 0, sizeof(LinkedStack));
	}
	else {
		printf("오류, 메모리할당,createLinkedStack()\n");
		return NULL;
	}

	return pReturn;
}

int pushLS(LinkedStack* pStack, struct BTreeNodeType* data)	//Linked_Stack에 B-트리 노트 타입의 데이터를 푸시
{
	int ret = 0;
	LinkedStackNode *pNode = NULL;	

	if (pStack != NULL) {
		pNode = (LinkedStackNode *)malloc(sizeof(LinkedStackNode));
		if (pNode != NULL) {
			pNode->data = data;					//새로운 노드에 들어온 데이터에 BTreeNodeType의 Data가 들어옴
			pNode->pLink = pStack->pTop;		//현재 linked_stack의 링크를 최상단 포인터인 top에 가리키게 함.
			pStack->pTop = pNode;				//top은 pNode를 가리키게 함.
			  
			pStack->currentCount++;		//stack 안에 데이터가 증가할 때마다 count증가
			ret = 1;
		}
		else {
			printf("오류, 메모리할당,pushLS()\n");
		}
	}

	return ret;
}

LinkedStackNode* popLS(LinkedStack* pStack)
{
	LinkedStackNode* pReturn = NULL;
	if (pStack != NULL)	{
		if (isLinkedStackEmpty(pStack) == 0) { // stack이 비어있지 않으면 
			pReturn = pStack->pTop; 		   // top 포인터를 가져와서
			pStack->pTop = pReturn->pLink;     // top포인터에는 해당 가져온 top포인터의 링크에 걸어두고
			pReturn->pLink = NULL;			   // 해당 link는 NULL처리

			pStack->currentCount--;			// count 감소
		}
	}

	return pReturn;
}

LinkedStackNode* peekLS(LinkedStack* pStack)
{
	LinkedStackNode* pReturn = NULL;
	if (pStack != NULL) {
		if (isLinkedStackEmpty(pStack) == 0) { //stack이 비어있지 않으면
			pReturn = pStack->pTop;   //스택의 top 포인터 가져오기
		}
	}

	return pReturn;
}

void deleteLinkedStack(LinkedStack* pStack)
{
	LinkedStackNode *pNode = NULL;
	LinkedStackNode *pDelNode = NULL;

	if (pStack != NULL) {
		pNode = pStack->pTop;
		while(pNode != NULL) {
			pDelNode = pNode;
			pNode = pNode->pLink;
			free(pDelNode);
		}
		free(pStack);
	}	
}

int isLinkedStackFull(LinkedStack* pStack)
{
	int ret = 0;

	/*
	현재 stack의 size가 나와있지 않으므로 일단 주석 처리
	if (pStack != NULL) {
		if (pStack->currentCount == MAX_SIZE) {
			ret = 1;
		}
	}
	*/
	return ret;
}

int isLinkedStackEmpty(LinkedStack* pStack)
{
	int ret = 0;

	if (pStack != NULL) {
		if (pStack->currentCount == 0) {
			ret = 1;
		}
	}

	return ret;
}
