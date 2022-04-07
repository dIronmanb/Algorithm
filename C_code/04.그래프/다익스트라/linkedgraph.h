#ifndef _LINKEDGRAPH_
#define _LINKEDGRAPH_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "linkedlist.h"

#define LINKED_GRAPH_TYPE_DIRECT         0  //  단방향
#define LINKED_GRAPH_TYPE_UNDIRECT       1  //  쌍방향

typedef struct LinkedGraphType
{
    int graphType;          // ??? LINKED_GRAPH_TYPE에 의해 결정되는 것인가?
    int nodeCount;          // 노드 개수
    LinkedList** ppAdjEdge;	// 간선 저장을 위한 연결 리스트 (포인터)의 배열
}  LinkedGraph;

// 연결 그래프 생성
LinkedGraph* createLinkedGraph(int graphType, int nodeCount);

// 그래프에서 해당 노드가 유효한지를 판별
int checkVertexValid(LinkedGraph* pGraph, int node);

// 두 노드를 사이의 간선을 연결
int addEdgeInternalLG( LinkedGraph* pGraph, int fromNode, int toNode, int weight);

// 
int addEdgeLG( LinkedGraph* pGraph, int fromNode, int toNode, int weight);

// 두 노드 사이의 간선을 삭제
int removeEdgeInternalLG(LinkedGraph* pGraph, int fromNode, int toNode);

//
int removeEdgeLG(LinkedGraph* pGraph, int fromNode, int toNode);

// 두 노드가 서로 연결되어 있는가
GraphEdge* getEdgeLG(LinkedGraph* pGraph, int fromNode, int toNode);

// display
void displayGraphLG( LinkedGraph* pGraph);

// delete
void deleteGraphLG( LinkedGraph* pGraph);

#endif

