#include <stdlib.h>
#include <math.h>

typedef struct {
    int val;
    int min;
} Node;

typedef struct {
    Node* data;
    int top;
    int capacity;
} MinStack;

MinStack* minStackCreate() {
    MinStack* obj = (MinStack*)malloc(sizeof(MinStack));
    obj->capacity = 10000;
    obj->data = (Node*)malloc(sizeof(Node) * obj->capacity);
    obj->top = -1;
    return obj;
}

void minStackPush(MinStack* obj, int val) {
    obj->top++;
    int currentMin = (obj->top == 0) ? val : (val < obj->data[obj->top - 1].min ? val : obj->data[obj->top - 1].min);
    obj->data[obj->top].val = val;
    obj->data[obj->top].min = currentMin;
}

void minStackPop(MinStack* obj) {
    obj->top--;
}

int minStackTop(MinStack* obj) {
    return obj->data[obj->top].val;
}

int minStackGetMin(MinStack* obj) {
    return obj->data[obj->top].min;
}

void minStackFree(MinStack* obj) {
    free(obj->data);
    free(obj);
}