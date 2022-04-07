#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "linkedlist.h"

LinkedList *createLinkedList() {
    LinkedList *pReturn = (LinkedList *)malloc(sizeof(LinkedList));
    memset(pReturn, 0, sizeof(LinkedList));
    return pReturn;
}

GraphEdge* getLinkedListData(LinkedList* pList, int position) {
    GraphEdge* ret = NULL;
    int i = 0;
    
    LinkedListNode *pCurrentNode = &(pList->headerNode); // List의 헤더노드의 주소값을 가져옴
    for (i = 0; i <= position; i++) {
        pCurrentNode = pCurrentNode->pLink; // 현 포지션을 향해서 다음 링크로 계속 이동
    }
    if (NULL != pCurrentNode) {
        ret = &(pCurrentNode->data); // 해당 포지션까지 도달시 ret에 해당 노드의 데이터를 얻어옴
    }
    
    return ret;
}

int addLinkedListData(LinkedList* pList, int position, GraphEdge data) {
    int i = 0;
    LinkedListNode *pNewNode = NULL;
    LinkedListNode *pPreNode = NULL;
    
    pNewNode = (LinkedListNode*)malloc(sizeof(LinkedListNode));
    pNewNode->data = data;
    
    pPreNode = &(pList->headerNode);   
    for (i = 0; i < position; i++) {
        pPreNode = pPreNode->pLink; // 해당 포지션까지 링크를 타고 계속 이동...
    }
    
    pNewNode->pLink = pPreNode->pLink;  // 그곳의 PreNode의 링크가 NewNode의 링크가 됨
    pPreNode->pLink = pNewNode;         // PreNode의 링크에는 NewNode을 가리키게 함.
    pList->currentCount++;              // 데이터가 증가했으니 count를 1증가
    return 1;
}

int removeLinkedListData(LinkedList* pList, int position) {
    int i = 0;
    LinkedListNode *pDelNode = NULL;
    LinkedListNode *pPreNode = NULL;
    
    pPreNode = &(pList->headerNode);
    for (i = 0; i < position; i++) {
        pPreNode = pPreNode->pLink; // 해당 포지션까지 링크를 타고 계속 이동...
    }
    
    pDelNode = pPreNode->pLink;
    pPreNode->pLink = pDelNode->pLink;
    free(pDelNode);
    pList->currentCount--;
    return 1;
}

void deleteLinkedList(LinkedList* pList) {
    LinkedListNode *pDelNode = NULL;
    LinkedListNode *pPreNode = pList->headerNode.pLink;
    while(pPreNode != NULL) {
        pDelNode = pPreNode;
        pPreNode = pPreNode->pLink;
        
        free(pDelNode);
    }
    
    free(pList);
}

int getLinkedListLength(LinkedList* pList) {
    if (NULL != pList) {
        return pList->currentCount; //현재 쌓여진 데이터 개수 = currentCount
    }
    return 0;
}


