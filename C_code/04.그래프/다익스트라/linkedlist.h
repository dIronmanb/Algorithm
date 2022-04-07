#ifndef _LINKEDLIST_
#define _LINKEDLIST_
// 연결 리스트에 대한 내용들

/*
    ( 노드 | 링크 ) -> ( 노드 | 링크 ) -> ( 노드 | 링크 )-> ...

*/

typedef struct GraphEdgeType {
    int toNodeID;		// 노드 ID
    int weight;			// 가중치.
} GraphEdge;

typedef struct LinkedListNodeType {
    GraphEdge data;
    struct LinkedListNodeType *pLink;
} LinkedListNode;

typedef struct LinkedListType {
    LinkedListNode  headerNode;     // 가장 처음의 헤더 노드
    int             currentCount;   // 쌓여진 데이터 개수
} LinkedList;

LinkedList *createLinkedList();
GraphEdge* getLinkedListData(LinkedList* pList, int position);
int addLinkedListData(LinkedList* pList, int position, GraphEdge data);
int removeLinkedListData(LinkedList* pList, int position);
void deleteLinkedList(LinkedList* pList);
int getLinkedListLength(LinkedList* pList);

#endif
