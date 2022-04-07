#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "linkedlist.h"
#include "linkedgraph.h"

/*
    연결 그래프의 구현을 자세히 살펴본다!
*/

LinkedGraph* createLinkedGraph(int graphType, int nodeCount)
{
    int i = 0;
    LinkedGraph *pReturn = NULL;
    
    if (nodeCount > 0)	{
        pReturn = ( LinkedGraph *)malloc(sizeof( LinkedGraph));
        if (pReturn == NULL) {
            printf("오류, 메모리할당(1), in createLinkedGraph()\n");
            return NULL;
        }
        pReturn->graphType = graphType;
        pReturn->nodeCount = nodeCount;
    }
    else {
        printf("오류, 최대 노드 개수는 0보다 커야합니다\n");
        return NULL;
    }
    
    pReturn->ppAdjEdge = (LinkedList **)malloc(sizeof(LinkedList*) * nodeCount); //간선이 double pointer로 되어 있으 
    if (pReturn->ppAdjEdge == NULL) {
        printf("오류, 메모리할당(3), in createLinkedGraph()\n");
        if (pReturn != NULL)  free(pReturn);
        return NULL;
    }
    for(i = 0; i < nodeCount; i++) {
        pReturn->ppAdjEdge[i] = createLinkedList(); //각 간선마다 연결 리스트를 생성
        if (pReturn->ppAdjEdge[i] == NULL) {
            printf("오류, 메모리할당(4), in createLinkedGraph()\n");
            if (pReturn->ppAdjEdge != NULL)  free(pReturn->ppAdjEdge);
            if (pReturn != NULL)  free(pReturn);
            return NULL;
        }
    }
    /*
        간선의 정보를 2차원 행렬로 담는다. 이때 길이 가변적임을 고려하여 이중포인터를 사용!
    */
    
    return pReturn;
}

int checkVertexValid(LinkedGraph* pGraph, int node) // 현재 그래프 Vertex가 유효한지를 검사
{
    if (pGraph != NULL && node >= 0 && node < pGraph->nodeCount) { //인자로 넘겨준 node의 타입이 int형, nodeCount에 부합하는지만 검사
        return 1;
    }
    else {
        return 0;
    }
}

int addEdgeInternalLG( LinkedGraph* pGraph, int fromNode, int toNode, int weight)
{
    int ret = 0;
    
    if (pGraph != NULL
        && checkVertexValid(pGraph, fromNode) /*그래프에서 현재 노드가 유효한지를 판단*/
        && checkVertexValid(pGraph, toNode)   /*그래프에서 다음 노드가 유효한지를 판단*/) {
        
        // 이전 노드에서 다음 노드간의 간선 및 가중치를 이중 포인터 ppAdjEgde에 저장
        GraphEdge data;
        data.toNodeID = toNode;
        data.weight = weight;
        addLinkedListData(pGraph->ppAdjEdge[fromNode], 0, data);
    }
    else {
        ret = -1;
    }
    
    return ret;
}

int addEdgeLG( LinkedGraph* pGraph, int fromNode, int toNode, int weight)
{
    int ret = 0;
    
    ret = addEdgeInternalLG(pGraph, fromNode, toNode, weight);

    if (0 == ret && LINKED_GRAPH_TYPE_UNDIRECT == pGraph->graphType) { //쌍방향이면 다음 노드와 이전 노드 사이에서도 간선을 연결
        ret = addEdgeInternalLG(pGraph, toNode, fromNode, weight);
    }
    
    return ret;
}

int removeEdgeInternalLG(LinkedGraph* pGraph, int fromNode, int toNode)
{
    int ret = -1;
    LinkedList *pList = NULL;
    int i = 0, count = 0;
    
    if (pGraph != NULL
        && checkVertexValid(pGraph, fromNode)
        && checkVertexValid(pGraph, toNode)) {
        pList = pGraph->ppAdjEdge[fromNode];
        count = getLinkedListLength(pList);
        for(i = 0; i < count; i++) {
            GraphEdge* pCurrent = getLinkedListData(pList, i);
            if (NULL != pCurrent && pCurrent->toNodeID == toNode) {
                removeLinkedListData(pList, i); // 연결 리스트에서 해당하는 i를 삭제
                ret = 0;
                break;
            }
        }
    }
    else {  // 해당되는 간선이 없는 경우 (삭제에 실패한 경우).
        ret = -1;
    }
    
    return ret;
}


int removeEdgeLG(LinkedGraph* pGraph, int fromNode, int toNode)
{
    int ret = -1;
    
    ret = removeEdgeInternalLG(pGraph, fromNode, toNode);
    if (0 == ret && LINKED_GRAPH_TYPE_UNDIRECT == pGraph->graphType) { //쌍방향이면 같이 삭제
        ret = removeEdgeInternalLG(pGraph, toNode, fromNode);
    }
    
    return ret;
}

GraphEdge* getEdgeLG(LinkedGraph* pGraph, int fromNode, int toNode)
{
    GraphEdge *ret = NULL;
    LinkedList *pList = NULL;
    int i = 0, count = 0;
    
    if (pGraph != NULL
        && checkVertexValid(pGraph, fromNode)
        && checkVertexValid(pGraph, toNode)) {
        pList = pGraph->ppAdjEdge[fromNode];
        count = getLinkedListLength(pList);
        for(i = 0; i < count; i++) {
            GraphEdge* pCurrent = getLinkedListData(pList, i);
            if (NULL != pCurrent && pCurrent->toNodeID == toNode) { // 이전 노드와 다음 노드가 여러 간선에 의해 연결되어 있는지를 판단: 연결 리스트 사용
                ret = pCurrent;
                break;
            }
        }
    }
    
    return ret;
}

void displayGraphLG( LinkedGraph* pGraph)
{
    int i = 0, j = 0, count = 0;
    
    if (pGraph != NULL) {
        count = pGraph->nodeCount;
        for(i = 0; i < count; i++)	{
            for(j = 0; j < count; j++) {
                GraphEdge* pEdge = getEdgeLG(pGraph, i, j);
                if (NULL != pEdge) {
                    printf("%d ", pEdge->weight);
                }
                else {
                    printf("0 ");
                }
            }
            printf("\n");
        }
    }
}

void deleteGraphLG( LinkedGraph* pGraph)
{
    int i = 0;
    
    if (pGraph != NULL) {
        for(i = 0; i < pGraph->nodeCount; i++) {
            deleteLinkedList(pGraph->ppAdjEdge[i]);
        }
        if (pGraph->ppAdjEdge != NULL) free(pGraph->ppAdjEdge);
        free(pGraph);
    }
}
/*

int main(int argc, char *argv[])
{
    int nodeCount = 6;
    LinkedGraph *pG1 = createLinkedGraph(LINKED_GRAPH_TYPE_UNDIRECT, nodeCount);
    if (pG1 != NULL) {
        addEdgeLG(pG1, 0, 1);
        addEdgeLG(pG1, 0, 2);
        addEdgeLG(pG1, 1, 2);
        addEdgeLG(pG1, 2, 3);
        addEdgeLG(pG1, 3, 4);
        addEdgeLG(pG1, 3, 5);
        addEdgeLG(pG1, 4, 5);
        
        printf("G1: 무방향 그래프\n");
        displayGraphLG(pG1);
        
        deleteGraphLG(pG1);
    }
    
    return 0;
}
 */
