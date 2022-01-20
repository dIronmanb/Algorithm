#ifndef _LINKEDLIST_
#define _LINKEDLIST_

#include "hashdef.h"

typedef struct LinkedListNodeType {
    HashSlot data;
    struct LinkedListNodeType *pLink;
} LinkedListNode;

typedef struct LinkedListType {
    LinkedListNode  headerNode;
    int             currentCount;
} LinkedList;

LinkedList *createLinkedList();
HashSlot* getLinkedListData(LinkedList* pList, int position);       
int addLinkedListData(LinkedList* pList, int position, HashSlot data);  // 해당 position에 HashSlot데이타를 넣음
int removeLinkedListData(LinkedList* pList, int position);
void deleteLinkedList(LinkedList* pList);
int getLinkedListLength(LinkedList* pList);

#endif
