#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "linkedlist.h"

LinkedList *createLinkedList() {
    LinkedList *pReturn = (LinkedList *)malloc(sizeof(LinkedList));
    memset(pReturn, 0, sizeof(LinkedList));
    return pReturn;
}

HashSlot* getLinkedListData(LinkedList* pList, int position) {
    HashSlot* ret = NULL;
    int i = 0;
    
    LinkedListNode *pCurrentNode = &(pList->headerNode);
    for (i = 0; i <= position; i++) {
        pCurrentNode = pCurrentNode->pLink;
    }
    if (NULL != pCurrentNode) {
        ret = &(pCurrentNode->data);
    }
    
    return ret;
}

int addLinkedListData(LinkedList* pList, int position, HashSlot data) {
    int i = 0;
    LinkedListNode *pNewNode = NULL;    // New node 생성
    LinkedListNode *pPreNode = NULL;    // postion만큼 뒤로 뺄 Pre node 생성
    
    pNewNode = (LinkedListNode*)malloc(sizeof(LinkedListNode));    // New node에는 LinkedListNode만큼의 메모리를 할당
    pNewNode->data = data;                                         // New node에 HashSlot 타입의 data를 넣음(실제 정보가 들어가는 공간 )
    
    pPreNode = &(pList->headerNode);   // LinkedList의 헤더를 pPreNode에 가져옴(계속 New node를 이어주기 위해서)
    for (i = 0; i < position; i++) {
        pPreNode = pPreNode->pLink;    // Postion동안 계속 뒤로,뒤로 링크타고 넘어감
    }
    
    pNewNode->pLink = pPreNode->pLink; // for문이 끝나고는: 여기에 NewNode의 link를 연결 -- 추후 다시 살펴보기
    pPreNode->pLink = pNewNode;        // NewNode는 PreNode가 연결
    pList->currentCount++;
    return 1;
}

int removeLinkedListData(LinkedList* pList, int position) {
    int i = 0;
    LinkedListNode *pDelNode = NULL;
    LinkedListNode *pPreNode = NULL;
    
    pPreNode = &(pList->headerNode);
    for (i = 0; i < position; i++) {
        pPreNode = pPreNode->pLink;
    }
    
    pDelNode = pPreNode->pLink;
    pPreNode->pLink = pDelNode->pLink;
    free(pDelNode);
    pList->currentCount--;
    return 1;
}

void deleteLinkedList(LinkedList* pList) {
    LinkedListNode *pDelNode = NULL;
    LinkedListNode *pPreNode = pList->headerNode.pLink; // plist의 헤더에 연결
    while(pPreNode != NULL) {
        pDelNode = pPreNode;        // 선 PreNode 주소를 받아옴
        pPreNode = pPreNode->pLink; // 후 PreNode의 다음 링크(주소)에 연결
        
        free(pDelNode);
    }
    
    free(pList);
}

int getLinkedListLength(LinkedList* pList) {
    if (NULL != pList) {
        return pList->currentCount; //현재 카운트된 값으로 연결 리스트의 크기를 알 수 있다.
    }
    return 0;
}


