int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int* answer = (int*)calloc(temperaturesSize, sizeof(int));
    *returnSize = temperaturesSize;
    
    int* stack = (int*)malloc(temperaturesSize * sizeof(int));
    int top = -1;

    for (int i = 0; i < temperaturesSize; i++) {
        while (top >= 0 && temperatures[i] > temperatures[stack[top]]) {
            int prevIndex = stack[top--];
            answer[prevIndex] = i - prevIndex;
        }
        stack[++top] = i;
    }

    free(stack);
    return answer;
}