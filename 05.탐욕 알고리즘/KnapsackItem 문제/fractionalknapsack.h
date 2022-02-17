#ifndef fractionalknapsack_h
#define fractionalknapsack_h

#include <stdio.h>
#include <stdlib.h>

typedef struct _KnapsackItem {
    char name[100];
    double weight;
    double profit;
    double selected;
} KnapsackItem;

// KnapsackItem포인터 타입 items은 입력과 출력의 역할을 모두 가진다.
void inputItems(KnapsackItem *items, int item_count);
double fractionalKnapsack(double capacity, KnapsackItem *items, int item_count);
void printResult(KnapsackItem *items, int item_count, double max_profit);

#endif
